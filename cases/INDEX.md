# Índice dos cases

Corpus Staff em PT-BR, primeira pessoa. Empregadores genéricos. Métricas: **resultado** (observado) vs **meta/alvo** (rotulado quando não for final medido).

Leitura de cases da indústria (link only): [docs/inspiracao.md](../docs/inspiracao.md).

| # | Arquivo | Tema | Período aprox. |
| --- | --- | --- | --- |
| 1 | [observabilidade-frontend.md](observabilidade-frontend.md) | Sentry em 4 fronts; tags; PII; chapter | ~2026 |
| 2 | [appsec-bff-go-live.md](appsec-bff-go-live.md) | Auditoria ASVS-L2; go-live bloqueado | ~2025–2026 |
| 3 | [ops-postmortems.md](ops-postmortems.md) | Grafana N3; cultura blameless | ~2026 |
| 4 | [checkout-idempotencia.md](checkout-idempotencia.md) | Race checkout/webhook | ~2026 |
| 5 | [feature-flag-pagamentos.md](feature-flag-pagamentos.md) | Rollout de reembolso + kill-switch | ~2026 |
| 6 | [falha-silenciosa-notificacoes.md](falha-silenciosa-notificacoes.md) | Push morto ~30 dias | ~2026 |
| 7 | [graphql-bff-clientes.md](graphql-bff-clientes.md) | REST → GraphQL BFF (OTT) | ~2019–2021 |

## Como usar este INDEX

1. Recrutador: leia o título + resultado; abra o arquivo se quiser o “como”.
2. Agent: não complete lacunas com nomes de empresa. Se faltar evidência, escreva `desconhecido`.
3. Eu: um case novo = um arquivo + uma linha aqui + uma linha em [`llms.txt`](../llms.txt).
