# Revisão de proposta, página de vendas e documento comercial

Vale para proposta comercial (PDF, Google Docs, deck), página de vendas, one-pager,
e-mail de oferta e script. O revisor lê como o cliente cético que vai decidir
sozinho, sem o vendedor do lado.

## Passo 1: triagem mecânica

```bash
python3 ~/.claude/skills/hormozi/scripts/triagem_copy.py proposta.md   # .txt, .md, .html
```

Mostra quais alavancas da equação de valor têm evidência no texto, a proporção
"você" contra "nós" e as palavras vagas. PDF: extraia o texto antes
(`pdftotext proposta.pdf -`).

## As quatro alavancas, para aplicar a rubrica sem abrir outro arquivo

Valor = (resultado dos sonhos x probabilidade percebida) ÷ (tempo até o
resultado x esforço e sacrifício). Resultado: o que o cliente ganha, em número
dele. Probabilidade: por que ele acredita que funciona para ele (prova parecida,
garantia, mecanismo). Tempo: quando sente a primeira vitória. Esforço: o que ele
precisa fazer ou largar. Detalhe e exemplos em `oferta.md`.

## Passo 2: rubrica de proposta (0 a 2 por linha, total 24)

| # | Critério | 0 | 1 | 2 |
| --- | --- | --- | --- | --- |
| 1 | Problema nas palavras do cliente | abre falando da empresa | problema genérico do setor | a dor deste cliente, com número dele |
| 2 | Custo de não fazer nada | ausente | citado | em R$ por mês ou por ano |
| 3 | Resultado dos sonhos | lista de entregáveis | resultado sem número | resultado com número e métrica que o cliente acompanha |
| 4 | Prazo e primeira vitória | ausente | prazo final só | cronograma com primeira vitória em dias |
| 5 | Esforço do cliente | ausente ou escondido | mencionado | explícito: o que ele faz e o que sai das costas dele |
| 6 | Prova | nenhuma | logo de cliente, depoimento genérico | caso parecido, com número e nome (13 critérios) |
| 7 | Mecanismo | caixa-preta | explicado com jargão | explicado com metáfora que o decisor repete |
| 8 | Reversão de risco | nenhuma | genérica | garantia com resultado e prazo, ou garantia implícita |
| 9 | Pacote e nome | itens soltos | pacote sem nome | pacote com nome (MAGIC) e bônus que respondem objeções |
| 10 | Preço ancorado | preço solto | comparado ao concorrente | ancorado no ganho ou no custo do problema, com opções |
| 11 | Objeções previstas | nenhuma | FAQ genérico | as objeções de cada decisor já respondidas |
| 12 | Próximo passo | "fico à disposição" | CTA genérico | ação, data, quem, e o que acontece depois de assinar |

Leitura: 0 a 10 reescreve (entregue as três mudanças e a proposta reescrita
inteira); 11 a 18 ajusta as linhas zeradas; 19 a 24 teste de preço e de opção,
a proposta está pronta.

## Passo 3: perguntas que a rubrica não pega

- **Mercado**: o cliente tem dor grande e dinheiro? Se não, diga isso antes de revisar texto.
- **Categoria de um**: dá para colocar esta proposta lado a lado com a do concorrente e comparar só preço? Se sim, falta diferenciação na oferta, não na redação.
- **Comitê**: quem mais lê isto sem você na sala? Cada um encontra a resposta dele? (`expansoes.md`, B2B)
- **Opções de preço**: existe âncora (versão maior) e uma saída menor (downsell) para não perder o cliente que acha caro? (`money-models.md`)
- **Legal**: garantia, escassez e urgência são reais e cumpríveis? (`expansoes.md`, CDC)

## Passo 4: formato da entrega

```
Nota: X/24. Veredito em uma frase: [o que mais impede o sim].

As 3 mudanças que mais aumentam a chance de fechar:
1. [trecho atual, citado] → [por que perde a venda: alavanca/critério] → [reescrita pronta]
2. ...
3. ...

Tabela da rubrica (12 linhas, nota e evidência de cada).

O que já está forte e não deve mexer: ...

Riscos: [legal, ético, promessa que a entrega não sustenta].
```

Regras: reescrita pronta para colar, na voz do documento original; cada
crítica ancorada num trecho citado; no máximo três mudanças principais, do maior
para o menor impacto no sim; o resto fica na tabela. Proposta inteira reescrita
só quando a nota fica em 10 ou menos, ou quando o usuário pede.
