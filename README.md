<!-- readme-padrao:header -->
<!-- Banner -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1a2e,100:00d9ff&height=200&section=header&text=hormozi&fontSize=54&fontColor=ffffff&animation=fadeIn&fontAlignY=36&desc=Claude%20Code%20skill%20for%20sales%20analysis%20with%20the%20Hormozi%20method&descAlignY=58&descSize=16" alt="hormozi" width="100%" />
</div>

<!-- Typing -->
<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=21&duration=2800&pause=900&color=00d9ff&center=true&vCenter=true&width=840&lines=Reviews+proposals%2C+copy%2C+ads+and+sales+conversations;Scored+rubric%2C+quoted+evidence%2C+rewrite+ready+to+paste;Hormozi+method+plus+B2B%2C+Brazilian+law%2C+Pix%2C+WhatsApp;3+stdlib+Python+scripts+with+TOON+output" alt="Reviews proposals, copy, ads and sales conversations" />
</div>

<div align="center">

  <p><strong>The three changes most likely to close more deals, with the current text and a ready rewrite.</strong></p>

  <p>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-00d9ff?style=for-the-badge" alt="License: MIT" /></a>
    <a href="https://docs.claude.com/en/docs/claude-code"><img src="https://img.shields.io/badge/Made%20for-Claude%20Code-D97757?style=for-the-badge&logo=anthropic&logoColor=white" alt="Made for: Claude Code" /></a>
    <img src="https://img.shields.io/badge/Python-3%20%C2%B7%20no%20dependencies-1a1a2e?style=for-the-badge&logo=python&logoColor=white" alt="Python: 3 · no dependencies" />
    <img src="https://img.shields.io/badge/modes-8-00d9ff?style=for-the-badge" alt="modes: 8" />
    <img src="https://img.shields.io/badge/skill%20language-PT--BR-00d9ff?style=for-the-badge" alt="skill language: PT-BR" />
    <a href="https://github.com/leonardocandiani/hormozi-skill/pulls"><img src="https://img.shields.io/badge/PRs-welcome-1a1a2e?style=for-the-badge" alt="PRs: welcome" /></a>
  </p>

  <p><a href="README.pt-BR.md">Leia em português</a></p>

  <p>
    <a href="#why-it-exists">Why it exists</a> •
    <a href="#modes">Modes</a> •
    <a href="#install">Install</a> •
    <a href="#usage">Usage</a> •
    <a href="#layout">Layout</a> •
    <a href="#sources-and-limits">Sources and limits</a> •
    <a href="#license">License</a>
  </p>
</div>

<br>

> **hormozi** reads your sales material like the skeptical buyer: it runs the mechanical triage, scores the mode's rubric and returns the three changes with the biggest impact on the yes, each with the quoted text and the new version to paste.

> Not affiliated with Alex Hormozi or Acquisition.com. Framework names belong to their authors; the summaries are written in original words.

## What it is

```yaml
product:  Claude Code skill to review and create sales material
modes:    document · copy · conversation · offer · revenue · funnel · closing · leads
based on: $100M Offers, Leads, Money Models and 10 playbooks from 2025
extends:  B2B committees, Brazilian consumer law, Pix, WhatsApp, ethics
scripts:  triagem_copy.py · analisar_conversa.py · funil.py
install:  git clone into ~/.claude/skills/hormozi
license:  MIT
```

<!-- /readme-padrao:header -->

A Claude Code skill that applies Alex Hormozi's sales method to real
commercial material: proposals, sales pages, copy, ads, WhatsApp threads,
call transcripts, price tables and funnel numbers. It reads like the skeptical
buyer, measures what can be measured and returns the three changes most likely
to close more deals, each one quoting the current text and giving a rewrite
ready to paste.

The skill itself is written in Brazilian Portuguese and tuned for Brazilian
businesses (consumer law, Pix, installments, WhatsApp as the main channel).
It answers in Portuguese.

## Why it exists

Hormozi's method is spread across three books and a dozen playbooks. Reviewing
a proposal with it means holding the value equation, the 13 proof criteria,
the layers of objections and the pricing plays in your head at once. The skill
packs that into scored rubrics and three scripts that count what a human
review tends to miss: price read as a promised result, a close that was never
asked for, a seller who kept talking after the yes.

It also goes past the method where the method stops: B2B deals with a buying
committee, Brazil's Consumer Defense Code, Pix and card installments, WhatsApp
as the sales channel, and the points where a close turns into manipulation.

## Modes

| You ask for | Mode | Rubric |
| --- | --- | --- |
| Review a proposal, deck, one-pager, sales page | Document | 12 criteria, score 0 to 24 |
| Analyze copy, post, ad, hook, script | Copy | 10 criteria, score 0 to 20 |
| "Why did this sale stall?" | Conversation | CLOSER, onion of blame, 5 cuts |
| Build or improve an offer, guarantee, bonus, name | Offer | Grand Slam Offer, step by step |
| Pricing, plans, price raise, LTV, churn | Revenue | 12 yes or no questions |
| Funnel numbers, CAC, bottleneck | Funnel | Stage rates, CAC, LTV:CAC, 30-day payback |
| Call script, objection answers, team drills | Closing | Closes by objection and the 28 rules |
| More leads, follow-up, show rate | Leads | Core Four and the 4 pillars of lead nurture |

The material picks the mode: "review this and tell me what to change to close
more" with a proposal attached is Document; with a conversation, it is
Conversation.

## Install

```bash
git clone https://github.com/leonardocandiani/hormozi-skill.git ~/.claude/skills/hormozi
```

Or keep the clone elsewhere and symlink it:

```bash
ln -s /path/to/clone ~/.claude/skills/hormozi
```

The scripts use only the Python 3 standard library. No dependencies.

## Usage

Inside Claude Code, ask in plain language: "revisa essa proposta pelo método
Hormozi", "por que essa conversa não fechou, a vendedora é a Ana", "monta uma
oferta pra clínica odontológica". The skill loads from its description.

The scripts also run straight from the terminal, with TOON output:

```bash
S=~/.claude/skills/hormozi/scripts

# Value equation levers with evidence in the text, customer focus, vague words
python3 $S/triagem_copy.py proposal.md

# Talk ratio, decision ask, objections by layer, words spoken after the yes
python3 $S/analisar_conversa.py thread.txt --vendedor "Ana" --full

# Stage rates, CAC, LTV:CAC, whether 30-day cash pays for CAC
python3 $S/funil.py --leads 400 --agendados 120 --compareceram 70 \
  --vendas 18 --gasto 9000 --caixa30 1200 --ltv 14400 --margem 0.6
```

The conversation analyzer reads WhatsApp exports (`[25/09/2026, 10:31:02] Name: text`
and `25/09/2026 10:31 - Name: text`), timestamped transcripts and plain
`Name: text` lines. All three exit with `error:` and `help:` and code 2 on
wrong usage.

## Layout

```
SKILL.md                     routing, doctrine and delivery format
references/
  oferta.md                  value equation, Grand Slam Offer, guarantees, MAGIC naming
  leads.md                   Core Four, ACA, rule of 100, 4 pillars of lead nurture
  copy-e-anuncios.md         hooks, awareness levels, 13 proof criteria, copy rubric
  fechamento.md              CLOSER, onion of blame, closes by objection, 28 rules
  money-models.md            attraction, upsell, downsell, continuity, pricing, LTV, retention
  conversas.md               call and WhatsApp analysis, delivery format
  propostas.md               proposal rubric and delivery format
  expansoes.md               B2B, consumer law, Pix, WhatsApp, ethics, weak evidence
scripts/
  triagem_copy.py            mechanical triage of copy and proposals
  analisar_conversa.py       sales conversation metrics
  funil.py                   funnel and unit economics diagnosis
```

## Sources and limits

Acquisition.com's 2025 playbooks (Closing, Lead Nurture, Hooks, GOATed Ads,
Proof Checklist, Pricing, Price Raise, Fast Cash, Lifetime Value, Retention)
were read in full and summarized in original words. $100M Offers, $100M Leads
and $100M Money Models came in through independent summaries that agree on
the technical names. Each reference marks how confident it is in what it states.

The books give no target close rate, show rate or talk ratio. When the skill
uses a threshold of its own, it says so. CLOSER comes from Hormozi's video
sales trainings and does not appear in the 2025 closing playbook.

The scripts count presence, not quality: a regex finds the word "garantia",
but it cannot tell whether the guarantee is any good. Judgment stays with the
rubric.

## License

MIT for this skill's code and text. The concepts and framework names belong
to Alex Hormozi and Acquisition.com.

<!-- readme-padrao:footer -->
<br>

---

<div align="center">
  <p><strong>Built by <a href="https://github.com/leonardocandiani">Leonardo Candiani</a></strong> · More projects at <a href="https://github.com/leonardocandiani?tab=repositories">github.com/leonardocandiani</a></p>
  <p>Leonardo Candiani builds AI agents that talk, decide and close deals. Cofounder of SixQuasar, operating Proteauto, SegSmart and IACall end to end.</p>
  <a href="https://leonardocandiani.com.br">
    <img src="https://img.shields.io/badge/-Website-0d1117?style=for-the-badge&logo=safari&logoColor=00d9ff" alt="Website" />
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
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00d9ff,50:1a1a2e,100:0d1117&height=120&section=footer&text=Thanks%20for%20stopping%20by&fontSize=18&fontColor=ffffff&fontAlignY=72" alt="Thanks for stopping by" width="100%" />
</div>
<!-- /readme-padrao:footer -->
