# Case rubric (Staff-grade)

What a Staff-grade case must make explicit: **problem**, **constraint**, **decision**, **evidence**, **outcome**. Language of the cases is PT-BR; this rubric is the English/PT contract so a reviewer (human or agent) can score the text without inventing employers.

This repo is narrative evidence (an INDEX), not a product. Mapa de leitura: [cases/INDEX.md](../cases/INDEX.md). Como editar: [CONTRIBUTING.md](../CONTRIBUTING.md).

Score **leverage**, not activity volume. A lista de PRs pessoais é sinal de sênior, não de Staff.

## How to score (promo packet)

| Axis | Staff-grade when | Fail when |
| --- | --- | --- |
| **Business / org impact** | Dinheiro, PII, seller, conversão, ou contrafactual honesto (incidente / go-live inseguro que **não** aconteceu) | “Entreguei a lib”; glue invisível sem estado antes/depois |
| **Technical depth** | Restrição, complexidade, alternativas recusadas, rollback / risco, evidência reproduzível (teste, ADR, rito) | Tutorial da ferramenta; sem limite |
| **Scope (teams)** | Superfícies e times nomeados de forma genérica; papel no rito: **autor**, **driver** ou **consultor** | “Liderei a migração” sem dizer quem dependia disso |
| **Decision + unmeasured** | O que foi aceito vs recusado **e** o que este texto **não mede** (meta/alvo/desconhecido) | Número único sem rótulo; OKR de mercado como medido; preencher lacuna com métrica inventada |

Frase útil (iniciativa → impacto → papel → times): *iniciei X; o custo de negócio era Y; meu papel foi driver/autor/consultor; N squads / superfícies dependiam disso.*

Projeto Staff (o que o packet pede, em público): o que eu fiz, impacto com meta clara, o que tornou complexo. Glue work (chapter, rito, onboarding) conta como impacto de org, não como vaidade de contagem. Evidência pública neste INDEX é o próprio case (ADR/RFC/postmortem em prosa). Sem wiki privada.

Densidade alvo: um Staff reader pontua perto de **8/10** quando os quatro eixos aparecem e a métrica é honesta. 10/10 exigiria close-out auditado com marca - isto é portfólio público, não data room.

## Five parts (estrutura do arquivo)

| Part | PT no case | Staff-grade when | Fail when |
| --- | --- | --- | --- |
| **Problem** | `## Problema` | Dor de negócio (dinheiro, PII, seller, conversão), não “faltava a lib” | Feature list, jargão sem custo |
| **Constraint** | explícita no contexto/problema | Tempo, LGPD, calendário, quota, superfície, “não parar o checkout” | História sem limite; parece playground |
| **Decision** | explícita em `## O que eu fiz` | Alternativas recusadas + o que foi aceito | Só a solução vencedora; sem trade-off |
| **Evidence** | teste, contagem, `path:line`, rito | Outro engenheiro reproduz o sinal sem wiki privada | “A gente viu”, ticket interno, DSN, host |
| **Outcome** | `## Resultado / métricas` | Tabela antes/depois; **resultado** vs **meta/alvo** rotulados | Número único sem rótulo; OKR de mercado como medido |

A abertura (antes de `## Problema`) tem de caber num fôlego: **Papel.** **Antes.** **Depois.** **Decisão.** **Não medido neste texto.**

## Required headings (CI)

Cada arquivo em `cases/*.md` (exceto `INDEX.md`) deve ter, nesta ordem:

1. `## Papel / período aproximado`
2. `## Contexto`
3. `## Problema`
4. `## O que eu fiz`
5. `## Resultado / métricas`
6. `## Aprendizados Staff`
7. `## Tags`

Check: `python3 scripts/check-case-headings.py`. Constraint e decision não são H2 extras; aparecem no texto como **Restrição.** e **Decisão.** A seção de resultado precisa de tabela com colunas Antes / Depois. Primeira pessoa: `Eu, Tiago Montanha`. A abertura precisa dos rótulos **Papel.** / **Antes.** / **Depois.** / **Decisão.** / `Não medido`.

## Before / after

A tabela de resultado deve ter colunas que um leitor descreia:

- Sinal (o que mudou)
- Antes (baseline observada ou “quase zero”)
- Depois (estado após a decisão)
- Rótulo: **Resultado** (observado) · **Meta** / **Alvo** (ainda não fechado) · **Qualitativo**

Contrafactual vale quando o texto já tem o estado evitado (go-live bloqueado, classe de duplicata sumiu, big bang de dinheiro recusado). Não invente “N incidentes evitados” se não mediu.

Arredonde. Prefira ordem de grandeza. Se o número não foi medido neste texto, escreva isso.

## Cross-links (this corpus + public standards)

Links que cabem aqui:

- Outro case deste repo, quando a classe de problema se repete (push morto e dashboard N3).
- Padrão público de terceiros (ex.: [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/), espírito SRE de postmortem).

Não cabe: wiki privada, Confluence, ADO, ticket interno. Não cabe lista de kits irmãos do mesmo GitHub - este INDEX se lê sozinho. Craft de packet (curadoria, não autoria): [docs/inspiracao.md](inspiracao.md).

## Authorship vs anonymity

Autoria: Tiago Montanha · Staff · [GitHub](https://github.com/tiagovilasboas) · [LinkedIn](https://www.linkedin.com/in/tiagovilasboas/). Empregadores: rótulos genéricos (marketplace de creators, checkout de alto volume, BFF de pagamentos, plataforma OTT). Primeira pessoa. Sem logo.

Exemplos mais densos nesta rubrica: [observabilidade-frontend.md](../cases/observabilidade-frontend.md), [appsec-bff-go-live.md](../cases/appsec-bff-go-live.md).
