# Feature flag de pagamentos: rollout de reembolso com kill-switch &lt; 30s

## Papel / período aproximado

Staff coordenando back de sellers e BFF/gateway de pagamentos. Período aproximado: 2026.

## Contexto

Um fix de reembolso (boleto + split, fluxo V5) precisava ir a produção sem apostar o livro-caixa num big bang. Dois serviços, mesmo comportamento de flag. Eu, Tiago Montanha, recusei “deploy e reza” e recusei flag no banco de um serviço só.

## Problema

- O caminho de reembolso já tinha **reaberturas** - fix parcial em fluxo multi-camada.
- Ligar 100% dos sellers no mesmo release é um incidente com botão de deploy.
- Flag local a um processo morre no pod ao lado.
- Sem bucketing determinístico, o mesmo seller oscila entre on/off a cada request - suporte vira loteria.

## O que eu fiz

1. **Serviço de flag compartilhado** - Redis entre back e gateway (mesmo store, sem acoplar schema SQL). Confirmei o store compartilhado na infra antes de apostar o desenho.
2. **Bucketing determinístico** por `seller_id` (hash estável → percentual). Rollout 1% → 10% → 50% → 100% sem “sorte”.
3. **Default OFF (fail-closed)** - o deploy do código **não** muda comportamento. Ligar é decisão explícita.
4. **Kill-switch operacional** - comando artisan (`set` / `status`) + healthcheck que expõe o estado. Sem rebuild, sem restart de pod.
5. **Dois PRs coordenados** (API + gateway) no mesmo contrato de nome de flag. Um só lado ligado = mentira.
6. **Docs curtos** para o N3: o que a flag faz, quem pode virar, o que observar no dashboard.

## Resultado / métricas

| Sinal | Rótulo |
| --- | --- |
| Tempo para desligar a flag em incidente | **&lt; 30s** - **resultado de capacidade** (comando + Redis), não um drill cronometrado publicado |
| Deploy do código sem mudar produção (default off) | **Resultado** |
| Mesmo seller, mesmo lado da flag, nos dois serviços | **Resultado** (bucketing + store compartilhado) |
| Zero regressão no livro de reembolso após 100% | **Alvo** do rollout - não publico aqui o close-out financeiro |

O valor Staff não é a lib de flag. É **coordenar dois times e um kill-switch** no caminho de dinheiro.

## Aprendizados Staff

- Feature flag de pagamento é controle de risco, não de marketing. Fail-closed.
- Determinismo &gt; percentual aleatório. Seller é a unidade de suporte.
- Kill-switch que exige pipeline não é kill-switch. Trinta segundos é o orçamento mental do N3.
- Coordenação &gt; código: o contrato do nome da flag e o store compartilhado são o design.

## Tags

`feature-flag` · `pagamentos` · `reembolso` · `redis` · `kill-switch` · `rollout`
