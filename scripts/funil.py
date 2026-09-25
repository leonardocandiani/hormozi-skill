#!/usr/bin/env python3
"""Diagnóstico de funil e economia de cliente pela lente Hormozi.

Calcula taxas por etapa, throughput, CAC, LTV:CAC, se o caixa dos primeiros
30 dias paga o CAC (aquisição financiada pelo cliente) e quanto cada alavanca
rende se melhorar 20%. Todos os campos são opcionais; o script calcula o que
os números informados permitem e diz o que faltou.

    funil.py --leads 400 --agendados 120 --compareceram 70 --vendas 18 \\
             --gasto 9000 --caixa30 2400 --ltv 14000 --margem 0.6

Campos: leads, agendados, compareceram, vendas (contagens do mesmo período);
gasto (marketing + vendas no período, R$); caixa30 (R$ recebido por cliente
nos primeiros 30 dias); ltv (R$ de receita por cliente na vida toda);
margem (bruta, 0 a 1).
"""
import sys

VERSAO = "1.0.0"
CAMPOS = ("leads", "agendados", "compareceram", "vendas", "gasto", "caixa30", "ltv", "margem")
ETAPAS = [("agendamento", "leads", "agendados"), ("comparecimento", "agendados", "compareceram"),
          ("fechamento", "compareceram", "vendas")]


def erro(msg, ajuda):
    print(f"error: {msg}\nhelp: {ajuda}")
    sys.exit(2)


def ler(argv):
    v, i = {}, 0
    while i < len(argv):
        chave = argv[i][2:] if argv[i].startswith("--") else None
        if chave not in CAMPOS:
            erro(f"argumento desconhecido {argv[i]}", "campos: --" + " --".join(CAMPOS))
        if i + 1 >= len(argv):
            erro(f"--{chave} sem valor", f"funil.py --{chave} 100")
        try:
            v[chave] = float(argv[i + 1].replace(",", "."))
        except ValueError:
            erro(f"--{chave} precisa de número, veio {argv[i + 1]}", f"funil.py --{chave} 100")
        i += 2
    return v


def reais(x):
    return "R$ " + f"{x:,.0f}".replace(",", ".")


def taxas(v):
    linhas, piores = [], []
    for nome, de, para in ETAPAS:
        if v.get(de) and para in v:
            t = v[para] / v[de]
            linhas.append(f"  {nome},{int(v[de])},{int(v[para])},{t:.0%}")
            piores.append((t, nome))
    return linhas, piores


def leitura_ltv(r):
    if r < 3:
        return "abaixo do mínimo de 3:1"
    return "ok para negócio sem humano; serviço pede 6:1 ou mais" if r < 6 else "saudável"


def economia(v):
    margem = v.get("margem", 1.0)
    faltou = [] if "margem" in v else ["margem (usei 100%, o que infla LTV:CAC e payback)"]
    if not (v.get("gasto") and v.get("vendas")):
        return ["cac: faltou --gasto e --vendas"], faltou
    cac = v["gasto"] / v["vendas"]
    saida = [f"cac: {reais(cac)}"]
    if v.get("ltv"):
        r = v["ltv"] * margem / cac
        saida.append(f"ltv_cac: {r:.1f}:1 sobre lucro bruto ({leitura_ltv(r)})")
    if v.get("caixa30"):
        lucro30 = v["caixa30"] * margem
        paga = "sim, cliente financia a aquisição" if lucro30 >= cac else f"não, faltam {reais(cac - lucro30)} por cliente"
        saida.append(f"payback_30_dias: {paga} (lucro bruto em 30 dias {reais(lucro30)} contra CAC {reais(cac)})")
    return saida, faltou


def alavancas(v):
    """Funil é multiplicativo: +20% em qualquer etapa rende +20% de vendas; nas quatro, 2,07x."""
    if not v.get("vendas"):
        return None
    extra = v["vendas"] * 0.2
    caixa = f" (+{reais(extra * v['caixa30'])} em 30 dias)" if v.get("caixa30") else ""
    return (f"alavancas: +20% em leads, agendamento, comparecimento OU fechamento = +{extra:.1f} vendas{caixa}; "
            f"nas quatro juntas = {v['vendas'] * 1.2 ** 4:.0f} vendas (2,07x). Mexa primeiro na mais barata de mover")


def main(argv):
    if "--version" in argv:
        print(VERSAO)
        return 0
    if not argv:
        erro("sem números", "funil.py --leads 400 --agendados 120 --compareceram 70 --vendas 18 --gasto 9000")
    v = ler(argv)
    linhas, piores = taxas(v)
    if linhas:
        print(f"etapas[{len(linhas)}]{{etapa,entrou,saiu,taxa}}:")
        print("\n".join(linhas))
    if v.get("leads") and v.get("compareceram"):
        print(f"throughput: {v['compareceram'] / v['leads']:.0%} dos leads chegam à call")
    if piores:
        t, nome = min(piores)
        print(f"menor_taxa: {nome} ({t:.0%}); compare com o seu histórico antes de chamar de gargalo")
    eco, faltou = economia(v)
    print("\n".join(eco))
    lav = alavancas(v)
    if lav:
        print(lav)
    if faltou:
        print(f"faltou[{len(faltou)}]: {'; '.join(faltou)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
