# Análise de conversa de venda (call transcrita, WhatsApp, e-mail)

Objetivo: achar onde a conversa perdeu a venda ou deixou dinheiro na mesa, e
dizer o que o vendedor fala diferente na próxima. Base: CLOSER, cebola da culpa
e as 28 regras (`fechamento.md`), pilares de nutrição (`leads.md`).

## Passo 1: números antes de opinião

```bash
python3 ~/.claude/skills/hormozi/scripts/analisar_conversa.py conversa.txt --vendedor "Nome" --full
```

O script mede proporção de fala, perguntas do vendedor, em que fala o preço
apareceu, se houve pedido de decisão (direto, ou só indireto como "posso te mandar
o link?", que pede permissão para um passo e não a compra), o sim do cliente e quanto o vendedor falou
depois, se saiu com próximo passo com data, e objeções por camada da cebola.
Regex conta presença; a leitura humana decide se a pergunta foi boa ou se a
objeção era real.

## Passo 2: ler a conversa em cinco cortes

**1. Estrutura (CLOSER).** Para cada letra, marque presente, fraca ou ausente, com
o número da fala como evidência.

- C: o cliente disse com as palavras dele por que veio? Ou o vendedor abriu apresentando a empresa?
- L: o vendedor nomeou o problema numa frase e o cliente confirmou?
- O: levantou o que ele já tentou e o custo disso?
- S: vendeu o resultado (a vida depois) ou descreveu entregável e processo?
- E: tratou objeções com validar, permissão, close, empilhar?
- R: depois do sim, reforçou a decisão e disse o que acontece a seguir, sem reabrir a venda?

**2. Objeções.** Liste cada uma com a camada (circunstância, outras pessoas, eu
mesmo), se foi a real ou a de superfície, e o que o vendedor fez. Erros comuns:
discutir em vez de validar; responder a primeira objeção como se fosse a
última; oferecer desconto (abandona o valor e vira barganha); aceitar "vou
pensar" sem perguntar o que faria virar um não.

**3. Momento do preço e do pedido.** Preço antes de o cliente sentir a dor
(etapas C, L, O) vira comparação. Conversa sem pedido explícito de venda é a
causa mais barata de consertar: o vendedor fez tudo e não pediu.

**4. Proporção de fala.** Não existe número do Hormozi para isso. Leitura
prática da skill: nas etapas C, L e O quem fala é o cliente; se o vendedor passa
de 60% da conversa inteira, ele provavelmente apresentou em vez de perguntar.

**5. Fim da conversa.** Saiu com próximo passo com data e hora (BAMFAM)? Se o
cliente disse sim, o vendedor parou de vender e passou para o pagamento?

Para WhatsApp, some os pilares de nutrição: tempo até a primeira resposta,
mensagens sem resposta do lado do vendedor, quantas tentativas antes de
desistir, lembrete antes da call.

## Passo 3: formato da entrega

```
Veredito: a venda [fechou | se perdeu | ficou em aberto] por [causa principal], na fala N.

Números: fala do vendedor X%, Y perguntas, preço na fala N, pedido [sim na fala N | não],
próximo passo [com data | sem data], objeções: [camadas].

O que custou a venda (ordem de impacto):
1. [fala N] o que aconteceu → por que custa (regra ou etapa) → o que falar no lugar:
   "frase pronta, na voz do vendedor"
2. ...

O que funcionou e deve repetir: [fala N] ...

Treino da semana: um obstáculo só (ex.: "vou pensar"), com 2 closes para ensaiar.
```

Regras da entrega: cada crítica cita o número da fala; cada correção vem com a
frase pronta que o vendedor diria; no máximo três pontos no "o que custou", do
maior para o menor impacto; um único tema de treino (é assim que o Hormozi
treinava o time: um obstáculo por vez).

## Analisar várias conversas (time ou período)

Rode o script em cada uma, junte as métricas numa tabela por vendedor
(comparecimento, fechamento, pedido de venda sim ou não, objeção mais comum) e
procure o padrão: a objeção que mais aparece aponta o que falta na oferta ou na
pré-venda, não só no vendedor. Regra 12 do playbook: se toda call vira batalha,
o problema está antes da call.
