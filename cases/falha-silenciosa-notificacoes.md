# Falha silenciosa de push: milhares sem notificação por ~30 dias

## Papel / período aproximado

Tech Lead N3, marketplace de creators. Período aproximado: 2026.

## Contexto

Push é o canal de “sua venda caiu / seu saque saiu”. Quando morre sem erro, o seller acha que a plataforma sumiu. Eu, Tiago Montanha, achei o buraco no **dashboard**, não na fila de tickets — e isso importa.

## Problema

Uma coorte grande — **milhares** de sellers (ordem de quatro mil, arredondado) — ficou **~30 dias** sem push. HTTP aparentava sucesso. Causa composta:

1. **API do provedor deprecada** / enforcement de autenticação que o client antigo não mandava.
2. **Sem checagem de falha** no client — não se lia “failed” no response; catch vazio ou `true` otimista.
3. **Sem alerta** de queda de entrega. Integração muda, ninguém acorda.
4. Breaking change de terceiro sem contrato de monitoramento.

Padrão sistêmico #1 daquele trimestre: falha silenciosa em integração externa.

## O que eu fiz

1. **Fix no client** — header de auth correto; tratar resposta de falha; log estruturado de erro (sem PII de device token em claro além do necessário).
2. **Fallback gracioso** — ausência de key não derruba o request de negócio; push falha, venda não. Trade-off: push pode falhar quieto se a key sumir — por isso o alerta existe.
3. **Testes** (~5) no caminho de falha, não só no happy path.
4. **Alertas** no APM/monitoramento de entrega do provedor (e canais irmãos: e-mail transacional).
5. **Painel N3** — taxa de envio / erro visível no dia seguinte, não no dia 31.
6. **Postmortem blameless** — a lição é “integração sem SLO de entrega”, não “quem esqueceu o header”.

## Resultado / métricas

| Sinal | Antes | Depois | Rótulo |
| --- | --- | --- | --- |
| Sellers sem push | milhares, ~30 dias | Canal restaurado após o deploy | **Resultado** |
| Tempo até detectar essa classe | semanas a **meses** no pior irmão de integração | **Meta:** &lt;24h via dashboard + alerta | meta |
| Testes no caminho de erro | 0 | ~5 | **Resultado** |
| Recorrência da mesma deprecação | possível | alerta + health de integração | **alvo** de não repetir cego |

Não publico token, não nomeio o vendor (está na lista de anonimização), não cito e-mail de seller.

## Aprendizados Staff

- Monitoramento que só vê HTTP 200 no *seu* server não vê o provedor deprecando o endpoint.
- `$response->failed()` (ou equivalente) é o teste de sanidade de toda integração. Happy path mente.
- Fallback gracioso sem alerta é o mesmo silêncio com nome bonito. Os dois juntos.
- Achar no dashboard é o ROI do case de [ops-postmortems.md](ops-postmortems.md). Sem painel, isso vira “seller sumiu e a gente não sabe”.

## Tags

`notificacoes` · `falha-silenciosa` · `integracao` · `alertas` · `n3`
