# Idempotência no checkout: race com webhook e vendas duplicadas

## Papel / período aproximado

Staff / Tech Lead full stack no checkout de um marketplace de creators. Período aproximado: 2026.

## Contexto

Checkout de alto volume + webhooks do gateway. Dois caminhos escrevem “venda”: a API do pagar e o evento assíncrono. Sem guarda compartilhada, o sistema cria duas vendas - ou uma venda e um órfão financeiro. Eu, Tiago Montanha, tratei isso como bug de **dinheiro**, não de log.

**Restrição.** Checkout não para para um “projeto de consistência”. Não dá para esperar `transaction_id` persistir antes do webhook. Não dá para bloquear upsell paralelo (duas ofertas distintas do mesmo comprador). Janela curta demais deixa passar checkout lento; janela longa castiga retry honesto.

## Problema

Race clássica no caminho quente:

1. Client retenta (timeout, double-click, gateway lento).
2. Webhook `charge.created` (ou equivalente) chega **antes** do `transaction_id` persistir - janela observada na ordem de **dezenas de segundos** em assinatura + cupom.
3. Segundo writer não encontra a venda e cria outra, às vezes com **valor do cupom** em vez do total.

| Dimensão | Antes (observado) |
| --- | --- |
| Writers da venda | API do pay + webhook, sem guarda compartilhada |
| Chave | `transaction_id` que ainda não existe |
| Janela | Ordem de 10s; falhava em checkout lento |
| Bordas | Upsell paralelo e subscription escapavam |
| Teste de corrida | Quase zero; hotfix reabria a janela |

Janela curta demais (ordem de 10s) falhava em checkout lento. Resultado: estorno, chargeback, seller descrente. Classe irmã no rito N3: [ops-postmortems.md](ops-postmortems.md).

## O que eu fiz

**Decisão.** Aceitei guarda durável na borda do pay **e** segundo guard no webhook, com Redis `SET NX` em **60s**. Recusei: só debounce no client (não sobrevive a retry do gateway), chave só em `transaction_id` nulo (o ID ainda não existe), janela de 10s (curta demais), janela de 120s (castiga retry honesto), um único middleware na API (não cobre a squad do webhook).

1. **Guarda durável na borda do pay** - middleware de idempotência. Chave derivada de identidade da tentativa (comprador + oferta + valor + meio + bucket de tempo), não de um ID que ainda não existe.
2. **Redis `SET NX` com TTL** - janela de **60s**. Trade-off explícito: compra legítima no 61º segundo pode passar; gateway &gt; 60s pode bloquear demais. ADR de uma página.
3. **Segundo guard no webhook** - para subscription, casar `payment_request_id` + tipo, não só `transaction_id` nulo.
4. **Bordas cobertas** - upsell paralelo (não colidir duas ofertas distintas), retry do gateway, ausência de `transaction_id`.
5. **Testes** - da ordem de **10** unitários de concorrência / chave / TTL. Sem teste, a janela volta a 10s no próximo “hotfix urgente”.
6. **Evidência no rito** - duplicata de dinheiro vira postmortem, não lore. Molde: timeline, evidência, ação com dono. Classe irmã: [ops-postmortems.md](ops-postmortems.md).

## Resultado / métricas

| Sinal | Antes | Depois | Rótulo |
| --- | --- | --- | --- |
| Classe “venda duplicada por race checkout/webhook” | Presente no caminho quente | Eliminada após o deploy da guarda | **Resultado** |
| Testes de idempotência no pacote do pay | Quase zero | ~10 (concorrência / chave / TTL) | **Resultado** |
| Janela da guarda | ~10s (falhava no checkout lento) | 60s (`SET NX`) | **Resultado** (trade-off, não lei) |
| Segundo writer (webhook) | Criava venda órfã | Guard por `payment_request_id` + tipo | **Resultado** |
| Chamado de estorno / duplicata | Baseline não publicada | Queda percebida pelo N3 | **Qualitativo** - não publico volume financeiro |
| Janela 60s ótima para todo o catálogo | - | Não é lei | **Não afirmado** |
| “Zero duplicata para sempre” | - | Mentira se afirmado | **Não afirmado** |

Zero **dessa classe**, com os guards no caminho quente, é o claim honesto.

## Aprendizados Staff

- Idempotência é padrão transversal. Um middleware numa API não conserta o webhook da squad ao lado - por isso o segundo guard.
- A chave é o design. Hash demais e você bloqueia upsell; hash de menos e você duplica.
- Teste de corrida é documentação executável do ADR. O número 60 só existe se o teste o protege.
- Dinheiro duplicado é o tipo de bug que o Staff puxa mesmo quando “não é da minha squad”.

## Tags

`checkout` · `idempotencia` · `redis` · `webhook` · `race` · `pagamentos`
