#!/usr/bin/env python3
"""Triagem mecânica de copy, proposta ou script de venda pela lente Hormozi.

Não julga a copy. Levanta sinais que dá pra contar (número, prazo, garantia,
prova, CTA, foco no cliente) para a análise humana começar do que falta.
Saída em TOON. Uso:

    triagem_copy.py arquivo.txt         # ou .md, .html
    pbpaste | triagem_copy.py -         # stdin
    triagem_copy.py arquivo.txt --full  # mostra todas as ocorrências
"""
import re
import sys
import html

VERSAO = "1.0.0"
MAX_EVID = 3

# Cada sinal: (id, alavanca da equação de valor ou etapa, regex, o que falta quando zera)
SINAIS = [
    ("numero_resultado", "resultado dos sonhos",
     r"(?:R\$\s?\d[\d.,]*|\d+[.,]?\d*\s?%|\b\d+[.,]?\d*\s?(?:mil|milh[õo]es|k)\b|\b\d{2,}\s+(?:clientes|leads|vendas|reuni[õo]es|pedidos|alunos|empresas|consultas|agendamentos|pacientes|contratos))",
     "promessa sem número: diga quanto (R$, %, quantidade)"),
    ("prazo", "atraso de tempo",
     r"\b(?:em|at[ée]|dentro de|nos primeiros|nas primeiras)\s+(?:\d+|um|uma|dois|duas|tr[êe]s|sete|quinze|trinta)\s+(?:minutos?|horas?|dias?|semanas?|meses|m[êe]s)\b|\bno mesmo dia\b|\bhoje mesmo\b|\bimediat",
     "sem prazo até o resultado: diga em quanto tempo o cliente vê algo"),
    ("baixo_esforco", "esforço e sacrifício",
     r"\bsem (?:precisar|ter que|contratar|saber|experi[êe]ncia|esfor[çc]o|trabalho)|\bfeito (?:pra|para) voc[êe]|\bn[óo]s fazemos|\ba gente faz|\bcuidamos d|\bautom[áa]tic|\bpronto (?:pra|para) usar|\bs[óo] (?:precisa|tem que)\b|\bvoc[êe] s[óo]\b",
     "não diz o que sai das costas do cliente (feito pra você, sem precisar de X)"),
    ("garantia", "probabilidade percebida",
     r"\bgarant(?:ia|imos|ido)|\breembols|\bdevolv\w*\s+(?:seu|o|100)|\bou (?:seu )?dinheiro de volta|\bsem risco|\bn[ãa]o paga\w* (?:se|at[ée])|\bs[óo] paga\w* (?:se|quando|depois)",
     "sem garantia nem reversão de risco"),
    ("prova", "probabilidade percebida",
     r"\bdepoiment|\bcase\b|\bcases\b|\bcaso de sucesso|\bclientes? como\b|\bresultados? (?:de|do|da|reais)|\bj[áa] (?:ajudamos|atendemos|entregamos|vendemos|formamos)|\b\d+\s*(?:\+\s*)?(?:clientes|empresas|alunos|projetos)\b|\bprint\b|\bantes e depois",
     "sem prova: caso com nome e número, depoimento, quantidade de clientes"),
    ("cta", "chamada para ação",
     r"\b(?:clique|clica|agende|agenda|responda|responde|chame|chama|fale|fala com|compre|garanta|acesse|inscreva|reserve|marque|mande|manda|assine|baixe|comece)\b|\bwa\.me\b|\blink (?:na|abaixo|da bio)",
     "sem pedido claro do próximo passo"),
    ("escassez", "reforço de oferta",
     r"\b(?:[úu]ltimas?|apenas|s[óo])\s+\d+\s+(?:vagas?|unidades?|lugares?)|\bvagas? limitad|\bestoque limitad|\bturma (?:fecha|limitada)",
     "sem escassez (opcional, só se for real)"),
    ("urgencia", "reforço de oferta",
     r"\bat[ée] (?:hoje|amanh[ãa]|domingo|segunda|ter[çc]a|quarta|quinta|sexta|s[áa]bado|o dia|\d{1,2}/\d{1,2})|\bencerra|\b[úu]ltim[oa] dia\b|\bs[óo] (?:hoje|esta semana|este m[êe]s)|\bprazo final",
     "sem urgência (opcional, só se for real)"),
    ("bonus", "reforço de oferta",
     r"\bb[ôo]nus\b|\bde brinde\b|\bgr[áa]tis\b|\bde presente\b|\bsem custo adicional",
     "sem bônus empilhado (opcional)"),
]

# Palavras que ocupam espaço sem mudar decisão de compra
# Linha com cara de preço cobrado: número dela não conta como resultado prometido
PRECO_LINHA = r"investimento|mensalidade|implanta[çc][ãa]o|\bpre[çc]o|\bvalor\b|\bcusta|\bparcela|\bsetup\b|\bplano\b|\btaxa\b"
VAGAS = r"\b(?:qualidade|excel[êe]ncia|solu[çc][õo]es|inovador\w*|inova[çc][ãa]o|completo|completa|l[íi]der|refer[êe]ncia|compromisso|parceiro ideal|o melhor|a melhor|diferenciad\w+|personalizad\w+|de ponta|sob medida|transformar|revolucion\w+|potencializ\w+|alavanc\w+)\b"
VOCE = r"\b(?:voc[êe]s?|seus?|suas?|te|contigo|cê)\b"
NOS = r"\b(?:n[óo]s|nossos?|nossas?|a gente|somos|nossa empresa|fomos|estamos)\b"


def ler_entrada(caminho):
    if caminho == "-":
        return sys.stdin.read()
    with open(caminho, encoding="utf-8") as f:
        texto = f.read()
    if caminho.endswith((".html", ".htm")):
        texto = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", texto, flags=re.S | re.I)
        texto = html.unescape(re.sub(r"<[^>]+>", " ", texto))
    return texto


def trecho(texto, m):
    """Contexto em volta do achado, cortado em fronteira de palavra."""
    ini, fim = max(0, m.start() - 35), min(len(texto), m.end() + 35)
    while ini > 0 and not texto[ini - 1].isspace():
        ini -= 1
    while fim < len(texto) and not texto[fim].isspace():
        fim += 1
    return " ".join(texto[ini:fim].split()).replace(",", ";")


def e_preco(texto, m):
    """Palavra de preço até 40 caracteres antes do número, na mesma linha."""
    antes = texto[max(0, m.start() - 40):m.start()].split("\n")[-1]
    return bool(re.search(PRECO_LINHA, antes, flags=re.I))


def erro(msg, ajuda):
    print(f"error: {msg}\nhelp: {ajuda}")
    sys.exit(2)


def ler_argumentos(argv):
    flags = [a for a in argv if a.startswith("--")]
    desconhecidas = [f for f in flags if f not in ("--full", "--version")]
    if desconhecidas:
        erro(f"flag desconhecida {desconhecidas[0]}", "flags aceitas: --full --version")
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        erro("faltou o texto", "triagem_copy.py arquivo.txt | pbpaste | triagem_copy.py -")
    try:
        return ler_entrada(args[0]), "--full" in flags
    except OSError as e:
        erro(f"não abri {args[0]} ({e.strerror})", "passe um caminho existente ou - para stdin")


def medir(texto, full):
    linhas, faltando = [], []
    for sid, alavanca, rx, falta in SINAIS:
        ms = list(re.finditer(rx, texto, flags=re.I))
        if sid == "numero_resultado":
            ms = [m for m in ms if not e_preco(texto, m)]
        evid = " | ".join(trecho(texto, m) for m in (ms if full else ms[:MAX_EVID]))
        linhas.append(f"  {sid},{alavanca},{len(ms)},\"{evid}\"" if ms else f"  {sid},{alavanca},0,-")
        if not ms:
            faltando.append((sid, falta))
    return linhas, faltando


def main(argv):
    if "--version" in argv:
        print(VERSAO)
        return 0
    texto, full = ler_argumentos(argv)
    palavras = len(re.findall(r"\w+", texto))
    if palavras == 0:
        erro("texto vazio", "confira o arquivo ou o conteúdo do stdin")
    linhas, faltando = medir(texto, full)
    zerados = {sid for sid, _ in faltando}
    obrig = {"numero_resultado", "prazo", "garantia", "prova", "cta", "baixo_esforco"}
    n_voce = len(re.findall(VOCE, texto, flags=re.I))
    n_nos = len(re.findall(NOS, texto, flags=re.I))
    vagas = sorted({v.lower() for v in re.findall(VAGAS, texto, flags=re.I)})

    print(f"texto: {palavras} palavras")
    print(f"alavancas_obrigatorias: {len(obrig - zerados)} de {len(obrig)} com evidência")
    print(f"sinais[{len(SINAIS)}]{{sinal,alavanca,ocorrencias,evidencia}}:")
    print("\n".join(linhas))
    alerta = " (fala mais de si que do cliente)" if n_nos > n_voce else ""
    print(f"foco_cliente: voce {n_voce}, nos {n_nos}{alerta}")
    print(f"palavras_vagas[{len(vagas)}]: {', '.join(vagas[:12]) or 'nenhuma'}")
    print(f"faltando[{len(faltando)}]{{sinal,o_que_fazer}}:")
    print("\n".join(f"  {sid},\"{falta}\"" for sid, falta in faltando) or "  nenhum sinal zerado")
    print("nota: regex acha presença, não qualidade. Leia a evidência e julgue pela references/copy-e-anuncios.md")
    if not full:
        print("dica: --full mostra todas as ocorrências de cada sinal")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
