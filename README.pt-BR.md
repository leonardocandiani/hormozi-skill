<!-- readme-padrao:header -->
<!-- Banner -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1a2e,100:00d9ff&height=200&section=header&text=hormozi&fontSize=54&fontColor=ffffff&animation=fadeIn&fontAlignY=36&desc=Skill%20do%20Claude%20Code%20para%20an%C3%A1lise%20comercial%20pelo%20m%C3%A9todo%20Hormozi&descAlignY=58&descSize=16" alt="hormozi" width="100%" />
</div>

<!-- Typing -->
<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=21&duration=2800&pause=900&color=00d9ff&center=true&vCenter=true&width=840&lines=Revisa+proposta%2C+copy%2C+an%C3%BAncio+e+conversa+de+venda;Nota+por+rubrica%2C+trecho+citado+e+reescrita+pronta;M%C3%A9todo+Hormozi+mais+B2B%2C+CDC%2C+Pix+e+WhatsApp;3+scripts+em+Python+puro%2C+sa%C3%ADda+em+TOON" alt="Revisa proposta, copy, anúncio e conversa de venda" />
</div>

<div align="center">

  <p><strong>As três mudanças que mais aumentam a chance de fechar, com o trecho atual e a reescrita pronta.</strong></p>

  <p>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-00d9ff?style=for-the-badge" alt="License: MIT" /></a>
    <a href="https://docs.claude.com/en/docs/claude-code"><img src="https://img.shields.io/badge/Made%20for-Claude%20Code-D97757?style=for-the-badge&logo=anthropic&logoColor=white" alt="Made for: Claude Code" /></a>
    <img src="https://img.shields.io/badge/Python-3%20%C2%B7%20no%20dependencies-1a1a2e?style=for-the-badge&logo=python&logoColor=white" alt="Python: 3 · no dependencies" />
    <img src="https://img.shields.io/badge/modes-8-00d9ff?style=for-the-badge" alt="modes: 8" />
    <img src="https://img.shields.io/badge/skill%20language-PT--BR-00d9ff?style=for-the-badge" alt="skill language: PT-BR" />
    <a href="https://github.com/leonardocandiani/hormozi-skill/pulls"><img src="https://img.shields.io/badge/PRs-welcome-1a1a2e?style=for-the-badge" alt="PRs: welcome" /></a>
  </p>

  <p><a href="README.md">Read in English</a></p>

  <p>
    <a href="#por-que-existe">Por que existe</a> •
    <a href="#modos">Modos</a> •
    <a href="#instalação">Instalação</a> •
    <a href="#uso">Uso</a> •
    <a href="#estrutura">Estrutura</a> •
    <a href="#fontes-e-limites">Fontes e limites</a> •
    <a href="#licença">Licença</a>
  </p>
</div>

<br>

> **hormozi** lê seu material comercial como o cliente cético: roda a triagem mecânica, passa a rubrica do modo e entrega as três mudanças de maior impacto no sim, cada uma com o trecho citado e a versão nova para colar.

> Sem afiliação com Alex Hormozi ou Acquisition.com. Os nomes dos frameworks pertencem aos autores; os resumos são escritos com palavras próprias.

## O que é

```yaml
produto:    skill do Claude Code para revisão e criação de material comercial
modos:      documento · copy · conversa · oferta · receita · funil · fechamento · leads
base:       $100M Offers, Leads, Money Models e 10 playbooks de 2025
expansões:  B2B com comitê, CDC, Pix e parcelamento, WhatsApp, limites éticos
scripts:    triagem_copy.py · analisar_conversa.py · funil.py
instalação: git clone em ~/.claude/skills/hormozi
licença:    MIT
```

<!-- /readme-padrao:header -->

Skill do Claude Code que aplica o método de vendas do Alex Hormozi em material
comercial de verdade: proposta, página de vendas, copy, anúncio, conversa de
WhatsApp, call transcrita, tabela de preço e números de funil. Ela lê como o
cliente cético, mede o que dá para medir e devolve as três mudanças que mais
aumentam a chance de fechar, cada uma com o trecho atual citado e a reescrita
pronta para colar.

## Por que existe

O método do Hormozi está espalhado em três livros e doze playbooks. Revisar
uma proposta com ele exige lembrar da equação de valor, dos 13 critérios de
prova, das camadas de objeção e das jogadas de preço ao mesmo tempo. A skill
junta isso em rubricas com nota e em três scripts que contam o que a leitura
humana costuma deixar passar: preço tratado como resultado, pedido de venda
que nunca aconteceu, vendedor que continuou falando depois do sim.

Ela também vai além do método onde ele não cobre: venda B2B com comitê de
compra, Código de Defesa do Consumidor, Pix e parcelamento, WhatsApp como
canal principal, e os pontos em que um close vira manipulação.

## Modos

| Você pede | Modo | Rubrica |
| --- | --- | --- |
| Revisar proposta, deck, one-pager, página de vendas | Documento | 12 critérios, nota de 0 a 24 |
| Analisar copy, post, anúncio, hook, roteiro | Copy | 10 critérios, nota de 0 a 20 |
| "Por que essa venda travou?" | Conversa | CLOSER, cebola da culpa, 5 cortes |
| Criar ou melhorar oferta, garantia, bônus, nome | Oferta | Grand Slam Offer passo a passo |
| Preço, planos, reajuste, LTV, churn | Receita | 12 perguntas de sim ou não |
| Números do funil, CAC, gargalo | Funil | Taxas, CAC, LTV:CAC, payback de 30 dias |
| Script de call, respostas a objeções, treino | Fechamento | Closes por objeção e as 28 regras |
| Mais leads, follow-up, comparecimento | Leads | Core Four e os 4 pilares de nutrição |

O material decide o modo: "revisa e me diz o que mudar pra fechar mais" com
uma proposta anexada vira Documento; com uma conversa, vira Conversa.

## Instalação

```bash
git clone https://github.com/leonardocandiani/hormozi-skill.git ~/.claude/skills/hormozi
```

Ou, mantendo o clone em outro lugar, um symlink:

```bash
ln -s /caminho/do/clone ~/.claude/skills/hormozi
```

Os scripts usam só a biblioteca padrão do Python 3. Nenhuma dependência.

## Uso

Dentro do Claude Code, peça em linguagem natural: "revisa essa proposta pelo
método Hormozi", "por que essa conversa não fechou, a vendedora é a Ana",
"monta uma oferta pra clínica odontológica". A skill carrega sozinha pela
descrição.

Os scripts também rodam direto no terminal, com saída em TOON:

```bash
S=~/.claude/skills/hormozi/scripts

# Alavancas da equação de valor com evidência no texto, foco no cliente, palavras vagas
python3 $S/triagem_copy.py proposta.md

# Proporção de fala, pedido de decisão, objeções por camada, fala depois do sim
python3 $S/analisar_conversa.py conversa.txt --vendedor "Ana" --full

# Taxas por etapa, CAC, LTV:CAC, se o caixa de 30 dias paga o CAC
python3 $S/funil.py --leads 400 --agendados 120 --compareceram 70 \
  --vendas 18 --gasto 9000 --caixa30 1200 --ltv 14400 --margem 0.6
```

O analisador de conversa lê export do WhatsApp (`[25/09/2026, 10:31:02] Nome: fala`
e `25/09/2026 10:31 - Nome: fala`), transcrição com hora e linhas `Nome: fala`.
Os três saem com `error:` e `help:` e código 2 quando o uso está errado.

## Estrutura

```
SKILL.md                     roteamento, doutrina e formato de entrega
references/
  oferta.md                  equação de valor, Grand Slam Offer, garantias, MAGIC
  leads.md                   Core Four, ACA, regra dos 100, 4 pilares de nutrição
  copy-e-anuncios.md         hooks, níveis de consciência, 13 critérios de prova, rubrica de copy
  fechamento.md              CLOSER, cebola da culpa, closes por objeção, 28 regras
  money-models.md            ofertas de atração, upsell, downsell, continuidade, preço, LTV, retenção
  conversas.md               análise de call e WhatsApp, formato de entrega
  propostas.md               rubrica de proposta e formato de entrega
  expansoes.md               B2B, CDC, Pix, WhatsApp, ética, onde a evidência é fraca
scripts/
  triagem_copy.py            triagem mecânica de copy e proposta
  analisar_conversa.py       métricas de conversa de venda
  funil.py                   diagnóstico de funil e economia do cliente
```

## Fontes e limites

Os playbooks de 2025 da Acquisition.com (Closing, Lead Nurture, Hooks, GOATed
Ads, Proof Checklist, Pricing, Price Raise, Fast Cash, Lifetime Value,
Retention) foram lidos na íntegra e resumidos com palavras próprias. $100M
Offers, $100M Leads e $100M Money Models entraram por resumos independentes
que batem entre si nos nomes técnicos. Cada referência marca a confiança do
que afirma.

A obra não traz meta de close rate, de comparecimento nem de proporção de
fala. Quando a skill usa um limiar próprio, ela diz que é dela. O CLOSER vem
dos treinamentos em vídeo do Hormozi e não aparece no playbook de fechamento
de 2025.

Os scripts contam presença, não qualidade: um regex acha a palavra "garantia",
mas não sabe se a garantia é boa. O julgamento fica com a rubrica.

## Licença

MIT para o código e o texto desta skill. Os conceitos e nomes de frameworks
pertencem a Alex Hormozi e à Acquisition.com.

<!-- readme-padrao:footer -->
<br>

---

<div align="center">
  <p><strong>Feito por <a href="https://github.com/leonardocandiani">Leonardo Candiani</a></strong> · Mais projetos em <a href="https://github.com/leonardocandiani?tab=repositories">github.com/leonardocandiani</a></p>
  <p>Leonardo Candiani constrói agentes de IA que conversam, decidem e fecham negócio. Cofundador da SixQuasar, operando Proteauto, SegSmart e IACall ponta a ponta.</p>
  <a href="https://leonardocandiani.com.br">
    <img src="https://img.shields.io/badge/-Site-0d1117?style=for-the-badge&logo=safari&logoColor=00d9ff" alt="Site" />
  </a>
  <a href="https://github.com/leonardocandiani">
    <img src="https://img.shields.io/badge/-GitHub-0d1117?style=for-the-badge&logo=github&logoColor=00d9ff" alt="GitHub" />
  </a>
  <a href="https://instagram.com/leonardocandiani">
    <img src="https://img.shields.io/badge/-Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram" />
  </a>
  <a href="https://youtube.com/@oleonardocandiani">
    <img src="https://img.shields.io/badge/-YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube" />
  </a>
</div>

<br>

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00d9ff,50:1a1a2e,100:0d1117&height=120&section=footer&text=Obrigado%20pela%20visita%21&fontSize=18&fontColor=ffffff&fontAlignY=72" alt="Obrigado pela visita!" width="100%" />
</div>
<!-- /readme-padrao:footer -->
