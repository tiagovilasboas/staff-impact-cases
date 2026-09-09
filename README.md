# Staff Impact Cases

Cases de impacto Staff (PT-BR), carreira anonimizada. Tiago Montanha.

Anonymized Staff career impact cases in PT-BR (GitHub SEO).

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

Mapa: [`cases/INDEX.md`](cases/INDEX.md). Rubrica Staff: [`docs/case-rubric.md`](docs/case-rubric.md). Índice máquina: [`llms.txt`](llms.txt).

| Case | Uma linha |
| --- | --- |
| [Observabilidade frontend](cases/observabilidade-frontend.md) | ~900 catches → Sentry em 4 fronts; tabela antes/depois |
| [AppSec no go-live do BFF](cases/appsec-bff-go-live.md) | ASVS-L2: bearer, IDOR, CORS; go-live bloqueado |
| [Ops e postmortems](cases/ops-postmortems.md) | Dashboard N3 + ~15 postmortems blameless |
| [Idempotência no checkout](cases/checkout-idempotencia.md) | Race checkout/webhook; duplicatas eliminadas |
| [Feature flag de pagamentos](cases/feature-flag-pagamentos.md) | Kill-switch &lt;30s sem redeploy |
| [Falha silenciosa de push](cases/falha-silenciosa-notificacoes.md) | Milhares sem notificação ~30 dias |
| [BFF GraphQL](cases/graphql-bff-clientes.md) | Dezenas de REST → um BFF para cliente limitado |

## Inspiração

Sou **apaixonado por estudar cases** de engenharia e frontend como ofício - decisão, evidência, trade-off. Leitura recomendada (não é autoria minha): [andrew--r/frontend-case-studies](https://github.com/andrew--r/frontend-case-studies). Como ler o catálogo externo versus estes textos: [`docs/inspiracao.md`](docs/inspiracao.md).

## Related

Kits públicos meus - não são evidência de que estes números rodaram numa marca nomeada.

- [sentry-golden-path](https://github.com/tiagovilasboas/sentry-golden-path) - golden path de erros, tracing, PII, tags
- [agentic-code-review](https://github.com/tiagovilasboas/agentic-code-review) - review AppSec: `path:line` ou silêncio
- [staff-postmortem](https://github.com/tiagovilasboas/staff-postmortem) - template blameless, evidence-first

## Tópicos (GitHub)

Sugestão de topics: `staff-engineer`, `case-study`, `observability`, `appsec`, `impact`.

## Contributing

Ver [`CONTRIBUTING.md`](CONTRIBUTING.md). Notas para agents: [`AGENTS.md`](AGENTS.md).

## License

[MIT](LICENSE).
