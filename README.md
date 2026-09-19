# Staff Impact Cases

Evidência narrativa de impacto Staff (PT-BR), carreira anonimizada. Tiago Montanha.

Isto **não** é um produto, CLI ou kit operacional. É um **INDEX de cases** para recrutador: cada arquivo é uma história com rubrica (problema, restrição, decisão, evidência, resultado). Meta e alvo são rótulos honestos quando o número não foi medido neste texto.

Anonymized Staff career impact cases in PT-BR (GitHub SEO). Narrative evidence, not a product.

Maintainer: [Tiago Montanha](https://github.com/tiagovilasboas) · Staff · [`@tiagovilasboas`](https://github.com/tiagovilasboas)

## Cases

| Case | Uma linha |
| --- | --- |
| [Observabilidade frontend](cases/observabilidade-frontend.md) | ~900 catches → Sentry em 4 fronts; tabela antes/depois |
| [AppSec no go-live do BFF](cases/appsec-bff-go-live.md) | ASVS-L2: bearer, IDOR, CORS; go-live bloqueado |
| [Ops e postmortems](cases/ops-postmortems.md) | Dashboard N3 + ~15 postmortems; before/after |
| [Idempotência no checkout](cases/checkout-idempotencia.md) | Race checkout/webhook; before/after; duplicatas da classe |
| [Feature flag de pagamentos](cases/feature-flag-pagamentos.md) | Kill-switch &lt;30s; before/after; fail-closed |
| [Falha silenciosa de push](cases/falha-silenciosa-notificacoes.md) | Milhares sem notificação ~30 dias; alerta + fallback |
| [BFF GraphQL](cases/graphql-bff-clientes.md) | Dezenas de REST → um BFF; before/after; client limitado |

Mapa: [`cases/INDEX.md`](cases/INDEX.md). Rubrica Staff: [`docs/case-rubric.md`](docs/case-rubric.md). Índice máquina: [`llms.txt`](llms.txt).

## Como ler

Score o case com a [rubrica](docs/case-rubric.md). Não some PRs, linhas ou reuniões.

1. **Impacto de negócio / org** - dinheiro, PII, seller, conversão, ou contrafactual honesto (o incidente / go-live que **não** aconteceu).
2. **Profundidade técnica** - restrição, complexidade, rollback, evidência (teste, ADR em prosa, rito).
3. **Escopo** - times ou superfícies tocados; papel no rito (**autor**, **driver**, **consultor**).
4. **Decisão + limite** - o que foi aceito vs recusado, e o que **não foi medido** neste texto (meta/alvo).

Frase útil: iniciativa → impacto de negócio → meu papel → times. A abertura de cada case cabe num fôlego (**Papel.** **Antes.** **Depois.** **Decisão.** **Não medido.**). Depois vem o “como”.

Exemplo pontuado (um case, quatro eixos, **~8.5**; 9+ seria close-out auditado com marca): [observabilidade-frontend na rubrica](docs/case-rubric.md#worked-example-observabilidade-frontend).

Empregadores genéricos. Sem ticket, DSN, host interno. Técnicas públicas (ASVS, espírito SRE) podem aparecer. Este INDEX não encaminha para um zoo de repositórios irmãos.

## Autoria

Eu, Tiago Montanha, escrevo estes cases em **primeira pessoa**. A autoria é minha; os empregadores não aparecem. Sem logo, sem ticket interno, sem DSN.

| | |
| --- | --- |
| Nome | Tiago Montanha |
| Papel | Staff |
| GitHub | [tiagovilasboas](https://github.com/tiagovilasboas) |
| LinkedIn | [tiagovilasboas](https://www.linkedin.com/in/tiagovilasboas/) |

**Disclaimer.** Empregadores anonimizados. Métricas ilustrativas ou arredondadas quando o número exato não cabe num texto público. Sem IP confidencial.

## Inspiração

Sou **apaixonado por estudar cases** de engenharia e frontend como ofício - decisão, evidência, trade-off. Leitura recomendada (não é autoria minha): [andrew--r/frontend-case-studies](https://github.com/andrew--r/frontend-case-studies). Como ler o catálogo externo versus estes textos: [`docs/inspiracao.md`](docs/inspiracao.md).

## Tópicos (GitHub)

Sugestão de topics: `staff-engineer`, `case-study`, `observability`, `appsec`, `impact`.

## Contributing

Ver [`CONTRIBUTING.md`](CONTRIBUTING.md). Notas para agents: [`AGENTS.md`](AGENTS.md).

## License

[MIT](LICENSE).
