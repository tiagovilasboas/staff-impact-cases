# Falha silenciosa de push: parte dos sellers sem notificação por ~30 dias

**Papel.** Driver e autor do fix no N3. **Antes.** Parte dos sellers sem push por ~30 dias; HTTP 200 mentia. **Depois.** Canal restaurado; ~5 testes no erro; alerta no painel. **Decisão.** Fix + alerta + fallback; recusei hotfix sem sinal. **Não medido neste texto.** meta &lt;24h ainda é meta; vendor e token ficam fora.

## Papel / período aproximado

Tech Lead N3, marketplace de creators. Período aproximado: 2026.

## Contexto

Push é o canal de “sua venda caiu / seu saque saiu”. Quando morre sem erro, o seller acha que a plataforma sumiu. Eu, Tiago Montanha, achei o buraco no **dashboard**, não na fila de tickets - e isso importa.

**Restrição.** Não nomear o vendor (lista de anonimização). Não publicar token ou e-mail de seller. Fallback não pode derrubar a venda. Calendário de N3: o canal precisa voltar sem esperar um projeto de plataforma.

## Problema

Uma fatia relevante dos sellers ficou **~30 dias** sem push. HTTP aparentava sucesso. Causa composta:

1. **API do provedor deprecada** / enforcement de autenticação que o client antigo não mandava.
2. **Sem checagem de falha** no client - não se lia “failed” no response; catch vazio ou `true` otimista.
3. **Sem alerta** de queda de entrega. Integração muda, ninguém acorda.
4. Breaking change de terceiro sem contrato de monitoramento.

Padrão sistêmico #1 daquele trimestre: falha silenciosa em integração externa.

| Dimensão | Antes (observado) |
| --- | --- |
| Entrega de push | HTTP 200 no *nosso* server; seller sem notificação |
| Coorte | Uma fatia relevante dos sellers, ~30 dias |
| Alerta de entrega | Ausente |
| Teste no caminho de falha | 0 |
| Onde achei | Dashboard N3, não a fila de tickets |

## O que eu fiz

**Decisão.** Aceitei fix no client + alerta + fallback gracioso + testes no caminho de falha. Recusei: só o hotfix do header (volta a falhar quieto), fallback sem alerta (o mesmo silêncio com nome bonito), testes só no happy path.

1. **Fix no client** - header de auth correto; tratar resposta de falha; log estruturado de erro (sem PII de device token em claro além do necessário).
2. **Fallback gracioso** - ausência de key não derruba o request de negócio; push falha, venda não. Trade-off: push pode falhar quieto se a key sumir - por isso o alerta existe.
3. **Testes** (~5) no caminho de falha, não só no happy path.
4. **Alertas** no APM/monitoramento de entrega do provedor (e canais irmãos: e-mail transacional).
5. **Painel N3** - taxa de envio / erro visível no dia seguinte, não no dia 31. ROI do case [ops-postmortems.md](ops-postmortems.md).
6. **Postmortem blameless** - a lição é “integração sem SLO de entrega”, não “quem esqueceu o header”.

## Resultado / métricas

| Sinal | Antes | Depois | Rótulo |
| --- | --- | --- | --- |
| Sellers sem push | parte da base, ~30 dias | Canal restaurado após o deploy | **Resultado** |
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
