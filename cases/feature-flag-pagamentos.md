# Feature flag de pagamentos: rollout de reembolso com kill-switch &lt; 30s

## Papel / período aproximado

Staff coordenando back de sellers e BFF/gateway de pagamentos. Período aproximado: 2026.

## Contexto

Um fix de reembolso (boleto + split, fluxo V5) precisava ir a produção sem apostar o livro-caixa num big bang. Dois serviços, mesmo comportamento de flag. Eu, Tiago Montanha, recusei “deploy e reza” e recusei flag no banco de um serviço só.

**Restrição.** Dois processos (API + gateway), sem acoplar schema SQL. Calendário de reembolso não parava. N3 precisa desligar sem rebuild e sem restart de pod. Seller é a unidade de suporte: o mesmo seller não pode oscilar on/off a cada request. Default do código tem que ser OFF.

## Problema

Dinheiro no meio. Flag de marketing não serve. O caminho de reembolso já tinha **reaberturas** (fix parcial em fluxo multi-camada). Ligar 100% dos sellers no mesmo release é um incidente com botão de deploy.

| Dimensão | Antes (observado) |
| --- | --- |
| Superfície do release | Big bang: 100% no mesmo deploy |
| Store da flag | Local a um processo; morre no pod ao lado |
| Bucketing | Sem determinismo; mesmo seller vira loteria |
| Kill-switch | Pipeline ou restart, se existia |
| Contrato entre API e gateway | Dois lados podiam mentir um ao outro |

## O que eu fiz

**Decisão.** Aceitei serviço de flag compartilhado em Redis, bucketing por `seller_id`, fail-closed e kill-switch operacional. Recusei: big bang 100%, flag numa tabela SQL de um serviço, percentual aleatório por request, “desliga no próximo deploy”, dois nomes de flag “quase iguais”.

1. **Serviço de flag compartilhado** - Redis entre back e gateway (mesmo store, sem acoplar schema SQL). Confirmei o store na infra antes de apostar o desenho.
2. **Bucketing determinístico** por `seller_id` (hash estável → percentual). Rollout 1% → 10% → 50% → 100% sem “sorte”.
3. **Default OFF (fail-closed)** - o deploy do código **não** muda comportamento. Ligar é decisão explícita.
4. **Kill-switch operacional** - comando artisan (`set` / `status`) + healthcheck que expõe o estado. Sem rebuild, sem restart de pod.
5. **Dois PRs coordenados** (API + gateway) no mesmo contrato de nome de flag. Um só lado ligado = mentira.
6. **Docs curtos para o N3** - o que a flag faz, quem pode virar, o que observar no dashboard. Painel irmão: [ops-postmortems.md](ops-postmortems.md). Incidente que dói dinheiro segue o molde de [staff-postmortem](https://github.com/tiagovilasboas/staff-postmortem).

## Resultado / métricas

| Sinal | Antes | Depois | Rótulo |
| --- | --- | --- | --- |
| Comportamento no deploy do código | Podia mudar no release | Default OFF; ligar é decisão | **Resultado** |
| Mesmo seller nos dois serviços | Podia divergir / oscilar | Mesmo lado da flag (hash + store) | **Resultado** |
| Tempo para desligar em incidente | Pipeline / restart | **&lt; 30s** (comando + Redis) | **Resultado** de capacidade, não drill cronometrado publicado |
| Store | Local a um processo | Redis compartilhado | **Resultado** |
| Rollout | Big bang ou sorte | 1% → 10% → 50% → 100% | **Resultado** |
| Zero regressão no livro de reembolso após 100% | Baseline de reabertura | Close-out financeiro | **Alvo** - não publico o número |

O valor Staff não é a lib de flag. É **coordenar dois times e um kill-switch** no caminho de dinheiro.

## Aprendizados Staff

- Feature flag de pagamento é controle de risco, não de marketing. Fail-closed.
- Determinismo &gt; percentual aleatório. Seller é a unidade de suporte.
- Kill-switch que exige pipeline não é kill-switch. Trinta segundos é o orçamento mental do N3.
- Coordenação &gt; código: o contrato do nome da flag e o store compartilhado são o design.

## Tags

`feature-flag` · `pagamentos` · `reembolso` · `redis` · `kill-switch` · `rollout`
