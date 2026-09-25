#!/usr/bin/env python3
"""Métricas mecânicas de uma conversa de venda (call transcrita ou WhatsApp).

Aceita linhas no formato "Nome: fala", export do WhatsApp
("[25/09/2026, 10:31:02] Nome: fala" ou "25/09/2026 10:31 - Nome: fala") e
transcrição com hora ("00:12:31 Nome: fala"). Quem é o vendedor vem por
--vendedor (parte do nome basta); sem ele, o script assume quem fala primeiro.

    analisar_conversa.py call.txt --vendedor Ana
    pbpaste | analisar_conversa.py - --vendedor "Ana Paula"
    analisar_conversa.py call.txt --full        # lista cada objeção achada

Saída em TOON. Não julga a call: dá os números para a leitura pela
references/conversas.md começar do que importa.
"""
import re
import sys

VERSAO = "1.0.0"

PREFIXOS = [
    r"^\[\d{1,2}/\d{1,2}/\d{2,4},? \d{1,2}:\d{2}(?::\d{2})?\]\s*",   # [25/09/2026, 10:31:02]
    r"^\d{1,2}/\d{1,2}/\d{2,4},? \d{1,2}:\d{2}(?::\d{2})?\s*-\s*",   # 25/09/2026 10:31 -
    r"^\(?\d{1,2}:\d{2}(?::\d{2})?\)?\s*",                            # 00:12:31 ou (12:31)
]
LINHA = re.compile(r"^([^:\n]{1,40}?):\s+(.+)$")

OBJECOES = {
    "circunstancia_tempo": r"\bsem tempo\b|\bn[ãa]o tenho tempo|\bcorrid[oa]\b|\bm[êe]s que vem\b|\bmais pra frente\b|\bagora n[ãa]o\b|\bn[ãa]o [ée] (?:a )?hora",
    "circunstancia_dinheiro": r"\bcar[oa]\b|\bn[ãa]o tenho (?:dinheiro|grana|verba|or[çc]amento)|\bsem (?:verba|or[çc]amento|grana)|\bpuxado\b|\bdesconto\b|\bmais barat",
    "circunstancia_fit": r"\bn[ãa]o [ée] pra mim|\bn[ãa]o serve\b|\bmeu caso [ée] diferente|\bn[ãa]o funciona (?:pra|no) m",
    "outros_decisor": r"\bmeu s[óo]cio|\bminha s[óo]cia|\bmeu marido|\bminha esposa|\bminha mulher|\bfalar com (?:o|a|meu|minha)|\bdiretoria\b|\bver com (?:o|a|meu|minha)|\baprova[çc][ãa]o",
    "outros_confianca": r"\bj[áa] (?:fui|me) (?:enganad|queimad|passad)|\bj[áa] contratei\b|\bj[áa] tentei\b|\bn[ãa]o confio|\bqual a diferen[çc]a|\bconcorrente\b|\boutra empresa",
    "eu_medo_adiar": r"\bpreciso pensar|\bvou pensar|\bdeixa eu pensar|\bme manda (?:o|um|a) (?:material|proposta|pdf)|\bdepois eu (?:vejo|te falo|respondo)|\bmedo\b|\binseguro\b|\bn[ãa]o sei se\b",
}
# Pedido direto: pede a decisão. Indireto: pede permissão para um passo (link, proposta), sem pedir a decisão.
PEDIDO_DIRETO = r"\bvamos fechar|\bfechamos\b|\bbora come[çc]ar|\bquer come[çc]ar|\bvamos come[çc]ar|\bvamos seguir\b|\bcomo (?:voc[êe] )?prefere pagar|\bpix ou cart[ãa]o|\bà vista ou parcelado|\bposso (?:gerar|emitir) (?:o|a) (?:contrato|cobran[çc]a|pix)|\best[áa] dentro\??|\bfaz sentido come[çc]ar"
PEDIDO_INDIRETO = r"\bposso te (?:mandar|enviar) (?:o|a) (?:link|proposta|contrato|pix)|\bte mando (?:o|a) (?:link|proposta|contrato)|\bquer que eu (?:mande|envie)"
SIM = r"^\s*(?:sim|fechado|bora|vamos|topo|pode mandar|manda o (?:link|pix|contrato)|pode ser|beleza,? vamos|ok,? vamos)\b"
PRECO = r"R\$\s?\d|\b\d+\s?(?:mil|reais)\b|\binvestimento\b|\bvalor [ée]\b|\bmensalidade\b"
PROXIMO_PASSO = r"\b(?:amanh[ãa]|segunda|ter[çc]a|quarta|quinta|sexta|s[áa]bado|domingo|dia \d{1,2}|\d{1,2}/\d{1,2}|[àa]s \d{1,2}(?:h|:\d{2}))\b"


def erro(msg, ajuda):
    print(f"error: {msg}\nhelp: {ajuda}")
    sys.exit(2)


def ler_argumentos(argv):
    full, vendedor, args, i = False, None, [], 0
    while i < len(argv):
        a = argv[i]
        if a == "--full":
            full = True
        elif a == "--vendedor":
            if i + 1 >= len(argv):
                erro("--vendedor sem nome", "analisar_conversa.py call.txt --vendedor Ana")
            vendedor, i = argv[i + 1], i + 1
        elif a.startswith("--"):
            erro(f"flag desconhecida {a}", "flags aceitas: --vendedor NOME --full --version")
        else:
            args.append(a)
        i += 1
    if not args:
        erro("faltou a conversa", "analisar_conversa.py call.txt --vendedor Ana | pbpaste | analisar_conversa.py -")
    try:
        texto = sys.stdin.read() if args[0] == "-" else open(args[0], encoding="utf-8").read()
    except OSError as e:
        erro(f"não abri {args[0]} ({e.strerror})", "passe um caminho existente ou - para stdin")
    return texto, vendedor, full


def falas(texto):
    """Lista de (quem, fala). Linha sem 'Nome:' continua a fala anterior."""
    saida = []
    for bruta in texto.splitlines():
        linha = bruta.strip().lstrip("‎")
        for p in PREFIXOS:
            linha = re.sub(p, "", linha)
        m = LINHA.match(linha)
        if m and not re.search(r"https?$", m.group(1)):
            saida.append([m.group(1).strip(), m.group(2).strip()])
        elif linha and saida:
            saida[-1][1] += " " + linha
    return [(q, f) for q, f in saida if "<Mídia oculta>" not in f and "<Media omitted>" not in f]


def e_vendedor(quem, vendedor):
    return vendedor.lower() in quem.lower()


def objecoes(conversa, vendedor):
    achadas = []
    for idx, (quem, fala) in enumerate(conversa):
        if e_vendedor(quem, vendedor):
            continue
        for camada, rx in OBJECOES.items():
            if re.search(rx, fala, flags=re.I):
                achadas.append((idx + 1, camada, fala[:70].replace(",", ";")))
    return achadas


def depois_do_sim(conversa, vendedor):
    """Palavras do vendedor entre o primeiro sim do cliente e o fim (regra 26: cale a boca)."""
    for idx, (quem, fala) in enumerate(conversa):
        if not e_vendedor(quem, vendedor) and re.search(SIM, fala, flags=re.I):
            resto = [f for q, f in conversa[idx + 1:] if e_vendedor(q, vendedor)]
            return idx + 1, sum(len(f.split()) for f in resto)
    return None, 0


def primeira_fala(conversa, vendedor, rx):
    return next((i + 1 for i, (q, f) in enumerate(conversa) if e_vendedor(q, vendedor) and re.search(rx, f, flags=re.I)), None)


def medir(conversa, vendedor):
    pv = [f for q, f in conversa if e_vendedor(q, vendedor)]
    pc = [f for q, f in conversa if not e_vendedor(q, vendedor)]
    palavras_v = sum(len(f.split()) for f in pv)
    total = max(palavras_v + sum(len(f.split()) for f in pc), 1)
    idx_sim, pos_sim = depois_do_sim(conversa, vendedor)
    achadas = objecoes(conversa, vendedor)
    return {
        "palavras_v": palavras_v, "total": total,
        "perguntas": sum(f.count("?") for f in pv),
        "preco": primeira_fala(conversa, vendedor, PRECO),
        "pedido": primeira_fala(conversa, vendedor, PEDIDO_DIRETO),
        "indireto": primeira_fala(conversa, vendedor, PEDIDO_INDIRETO),
        "sim": idx_sim, "pos_sim": pos_sim,
        "proximo": bool(re.search(PROXIMO_PASSO, " ".join(pv[-3:]), flags=re.I)),
        "achadas": achadas,
    }


def imprimir(m, n_falas, vendedor, full):
    achadas = m["achadas"]
    camadas = ", ".join(sorted({c for _, c, _ in achadas})) or "nenhuma detectada"
    if m["pedido"]:
        pedido = f"direto na fala {m['pedido']}"
    elif m["indireto"]:
        pedido = f"só indireto na fala {m['indireto']} (pediu permissão para um passo, não a decisão)"
    else:
        pedido = "não pediu"
    alerta = " (regra 26: depois do sim, cale a boca)" if m["pos_sim"] > 60 else ""
    sim = f"fala {m['sim']}, vendedor falou mais {m['pos_sim']} palavras depois{alerta}" if m["sim"] else "não detectado"
    proximo = "sim" if m["proximo"] else "não (BAMFAM: sair com a próxima reunião marcada)"
    print(f"conversa: {n_falas} falas, vendedor '{vendedor}'")
    print(f"fala_vendedor: {100 * m['palavras_v'] // m['total']}% das palavras ({m['palavras_v']} de {m['total']})")
    print(f"perguntas_vendedor: {m['perguntas']}")
    print(f"preco_mencionado_na_fala: {m['preco'] or 'nunca'}")
    print(f"pedido_de_decisao: {pedido}")
    print(f"sim_do_cliente: {sim}")
    print(f"proximo_passo_com_data: {proximo}")
    print(f"objecoes[{len(achadas)}] camadas: {camadas}")
    if full and achadas:
        print(f"objecoes_detalhe[{len(achadas)}]{{fala,camada,trecho}}:")
        print("\n".join(f"  {i},{c},\"{t}\"" for i, c, t in achadas))
    elif achadas:
        print("dica: --full lista cada objeção com o número da fala")
    print("nota: métricas contam, não julgam. Leia a conversa pela references/conversas.md")


def main(argv):
    if "--version" in argv:
        print(VERSAO)
        return 0
    texto, vendedor, full = ler_argumentos(argv)
    conversa = falas(texto)
    if len(conversa) < 2:
        erro("não achei falas no formato 'Nome: texto'", "confira o formato; export do WhatsApp e 'Nome: fala' funcionam")
    vendedor = vendedor or conversa[0][0]
    if not any(e_vendedor(q, vendedor) for q, _ in conversa):
        nomes = ", ".join(sorted({q for q, _ in conversa})[:6])
        erro(f"ninguém na conversa bate com --vendedor {vendedor}", f"participantes: {nomes}")
    imprimir(medir(conversa, vendedor), len(conversa), vendedor, full)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
