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

Densidade alvo deste corpus: um Staff reader pontua perto de **~8.5/10** quando os quatro eixos aparecem, a abertura cabe num fôlego e a métrica é honesta (resultado vs meta/alvo). **9+** exigiria close-out auditado com marca (data room). 10/10 não é o jogo deste INDEX. Calibração: [worked example abaixo](#worked-example-observabilidade-frontend).

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

Exemplo pontuado (um case, quatro eixos): [worked example](#worked-example-observabilidade-frontend). Outro texto denso no mesmo bar: [appsec-bff-go-live.md](../cases/appsec-bff-go-live.md).

## Worked example (observabilidade-frontend)

Score de [observabilidade-frontend.md](../cases/observabilidade-frontend.md) nos **quatro eixos**. Honesto. Sem métrica inventada para fechar o número.

| Axis | Score | Why this text lands here | What 9+ would need |
| --- | --- | --- | --- |
| **Business / org impact** | ~8.5 | Dor é receita e LGPD, não “faltava o SDK”: HTTP 200 no BFF + TypeError no botão pagar; ~900 `catch` vazios (contagem estática); seller/comprador sem stack. Chapter como glue de org (um padrão × quatro fronts). | Close-out de conversão ou crash-free **assinado** no trimestre, com marca. Este texto recusa “60% dos bugs” e “99,5% crash-free” - são OKR de mercado, não Resultado. |
| **Technical depth** | ~8.5 | **Restrição.** explícita (4 repos, LGPD, quota, calendário). Alternativas recusadas: só APM, sampling 100%, `captureException` nu, big bang, replay sempre ligado. Contrato de tags + `beforeSend`. | `path:line` de init/máscara, auditoria de quota do vendor, dump de source map. Isso é data room, não portfólio público. |
| **Scope (teams)** | ~8.5 | Papel no rito: **driver** do padrão, **autor** do chapter, **consultor** das squads de FE. Quatro superfícies nomeadas de forma genérica (checkout, dois painéis, admin). “Cinco squads” é ordem de grandeza, não headcount. | Organograma com nomes de time e % de adoção por repo. Anonimato correto impede isso. Não invento o percentual. |
| **Decision + unmeasured** | ~9 | Abertura num fôlego lista o recusado **e** o que **não** se mede. Tabela Sinal / Antes / Depois / Rótulo: detecção &lt;24h, taxa de incidente e MTTR ficam **meta/alvo**. | Publicar MTTR e crash-free como **Resultado** depois do trimestre fechar, auditado. Sem esse close-out, afirmar o número seria mentira. |

**Overall: ~8.5 / 10.** Os quatro eixos estão visíveis; a métrica é rotulada; o empregador é genérico. O teto não é prosa fraca. O teto é o que um INDEX público não pode carregar.

**9+ é close-out auditado com marca** (data room): empregador nomeado, rates do trimestre fechados, atribuição de conversão assinada, evidência `path:line` ou ticket interno. Este repositório **não** inventa esses números para caçar 9. Um 7.5 seria o mesmo case sem abertura, sem recusas ou com OKR de mercado colado como medido.

O que o case **já tem** (não acrescente precisão falsa):

- ~900 catches silenciosos como **Resultado** (contagem estática + adoção)
- Quatro projetos, tags `domain`/`flow`, máscara de PII como **Resultado**
- Latência &lt;24h, taxa de incidente, MTTR de checkout como **meta/alvo**

O que o case **recusa** com razão:

- crash-free 99,5%
- “60% dos bugs antes do suporte”
- MTTR final em minutos como se o trimestre tivesse fechado neste texto
