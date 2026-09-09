# Staff Impact Cases

Anonymized Staff career impact cases in PT-BR. | Cases de impacto Staff anonimizados, em português do Brasil.

Maintainer: [Tiago Montanha](https://github.com/tiagovilasboas) · Staff · [`@tiagovilasboas`](https://github.com/tiagovilasboas)

## Autoria

Eu, Tiago Montanha, escrevo estes cases em **primeira pessoa**. A autoria é minha; os empregadores não aparecem. Sem logo, sem ticket interno, sem DSN.

| | |
| --- | --- |
| Nome | Tiago Montanha |
| Papel | Staff |
| GitHub | [tiagovilasboas](https://github.com/tiagovilasboas) |
| LinkedIn | [tiagovilasboas](https://www.linkedin.com/in/tiagovilasboas/) |

**Disclaimer.** Empregadores anonimizados. Métricas ilustrativas ou arredondadas quando o número exato não cabe num texto público. Sem IP confidencial.

## Conteúdo

Mapa: [`cases/INDEX.md`](cases/INDEX.md). Índice máquina: [`llms.txt`](llms.txt).

| Case | Uma linha |
| --- | --- |
| [Observabilidade frontend](cases/observabilidade-frontend.md) | ~900 catches silenciosos → Sentry em 4 fronts |
| [AppSec no go-live do BFF](cases/appsec-bff-go-live.md) | ASVS-L2: bearer, IDOR, CORS; go-live bloqueado |
| [Ops e postmortems](cases/ops-postmortems.md) | Dashboard N3 + ~15 postmortems blameless |
| [Idempotência no checkout](cases/checkout-idempotencia.md) | Race checkout/webhook; duplicatas eliminadas |
| [Feature flag de pagamentos](cases/feature-flag-pagamentos.md) | Kill-switch &lt;30s sem redeploy |
| [Falha silenciosa de push](cases/falha-silenciosa-notificacoes.md) | Milhares sem notificação ~30 dias |
| [BFF GraphQL](cases/graphql-bff-clientes.md) | Dezenas de REST → um BFF para cliente limitado |

## Inspiração

Sou **apaixonado por estudar cases** de engenharia e frontend como ofício — decisão, evidência, trade-off. Leitura recomendada (não é autoria minha): [andrew--r/frontend-case-studies](https://github.com/andrew--r/frontend-case-studies). Como ler o catálogo externo versus estes texts: [`docs/inspiracao.md`](docs/inspiracao.md).

## Related

Kits públicos meus — não são evidência de que estes números rodaram numa marca nomeada.

- [sentry-golden-path](https://github.com/tiagovilasboas/sentry-golden-path) — golden path de erros, tracing, PII, tags
- [staff-postmortem](https://github.com/tiagovilasboas/staff-postmortem) — template blameless, evidence-first
- [nuxt-layered-boilerplate](https://github.com/tiagovilasboas/nuxt-layered-boilerplate) — Dependency Rule, port, BFF
- [frontend-case-studies](https://github.com/andrew--r/frontend-case-studies) — inspiração / leitura (terceiros)

## Tópicos (GitHub)

Sugestão de topics: `staff-engineer`, `case-study`, `observability`, `appsec`, `impact`.

## Contributing

Ver [`CONTRIBUTING.md`](CONTRIBUTING.md). Notas para agents: [`AGENTS.md`](AGENTS.md).

## License

[MIT](LICENSE).
