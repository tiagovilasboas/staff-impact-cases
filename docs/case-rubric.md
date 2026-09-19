# Case rubric (Staff-grade)

What a Staff-grade case must make explicit: **problem**, **constraint**, **decision**, **evidence**, **outcome**. Language of the cases is PT-BR; this rubric is the English/PT contract so a reviewer (human or agent) can score the text without inventing employers.

This repo is narrative evidence (an INDEX), not a product. Mapa de leitura: [cases/INDEX.md](../cases/INDEX.md). Como editar: [CONTRIBUTING.md](../CONTRIBUTING.md).

## Five parts

| Part | PT no case | Staff-grade when | Fail when |
| --- | --- | --- | --- |
| **Problem** | `## Problema` | Dor de negócio (dinheiro, PII, seller, conversão), não “faltava a lib” | Feature list, jargão sem custo |
| **Constraint** | explícita no contexto/problema | Tempo, LGPD, calendário, quota, superfície, “não parar o checkout” | História sem limite; parece playground |
| **Decision** | explícita em `## O que eu fiz` | Alternativas recusadas + o que foi aceito | Só a solução vencedora; sem trade-off |
| **Evidence** | teste, contagem, `path:line`, rito | Outro engenheiro reproduz o sinal sem wiki privada | “A gente viu”, ticket interno, DSN, host |
| **Outcome** | `## Resultado / métricas` | Tabela antes/depois; **resultado** vs **meta/alvo** rotulados | Número único sem rótulo; OKR de mercado como medido |

Densidade alvo deste corpus: narrativa que um Staff reader pontua perto de **8/10** (todas as cinco partes visíveis, métrica honesta, empregador genérico). 10/10 exigiria close-out auditado com marca - isto é portfólio público, não data room. Meta neste INDEX é rótulo honesto, não gap a tapar com número inventado.

## Required headings (CI)

Cada arquivo em `cases/*.md` (exceto `INDEX.md`) deve ter, nesta ordem:

1. `## Papel / período aproximado`
2. `## Contexto`
3. `## Problema`
4. `## O que eu fiz`
5. `## Resultado / métricas`
6. `## Aprendizados Staff`
7. `## Tags`

Check: `python3 scripts/check-case-headings.py`. Constraint e decision não são H2 extras; aparecem no texto como **Restrição.** e **Decisão.** (o check falha se faltarem). A seção de resultado precisa de tabela com colunas Antes / Depois. Primeira pessoa: `Eu, Tiago Montanha`.

## Before / after

A tabela de resultado deve ter colunas que um leitor descreia:

- Sinal (o que mudou)
- Antes (baseline observada ou “quase zero”)
- Depois (estado após a decisão)
- Rótulo: **Resultado** (observado) · **Meta** / **Alvo** (ainda não fechado) · **Qualitativo**

Arredonde. Prefira ordem de grandeza. Se o número não foi medido neste texto, escreva isso.

## Cross-links (this corpus + public standards)

Links que cabem aqui:

- Outro case deste repo, quando a classe de problema se repete (push morto e dashboard N3).
- Padrão público de terceiros (ex.: [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/), espírito SRE de postmortem).

Não cabe: wiki privada, Confluence, ADO, ticket interno. Não cabe lista de kits irmãos do mesmo GitHub - este INDEX se lê sozinho. Inspiração de terceiros: [docs/inspiracao.md](inspiracao.md) (link only).

## Authorship vs anonymity

Autoria: Tiago Montanha · Staff · [GitHub](https://github.com/tiagovilasboas) · [LinkedIn](https://www.linkedin.com/in/tiagovilasboas/). Empregadores: rótulos genéricos (marketplace de creators, checkout de alto volume, BFF de pagamentos, plataforma OTT). Primeira pessoa. Sem logo.

Exemplos mais densos nesta rubrica: [observabilidade-frontend.md](../cases/observabilidade-frontend.md), [appsec-bff-go-live.md](../cases/appsec-bff-go-live.md).
