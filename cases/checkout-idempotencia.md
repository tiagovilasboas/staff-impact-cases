# Idempotência no checkout: race com webhook e vendas duplicadas

## Papel / período aproximado

Staff / Tech Lead full stack no checkout de um marketplace de creators. Período aproximado: 2026.

## Contexto

Checkout de alto volume + webhooks do gateway. Dois caminhos escrevem “venda”: a API do pagar e o evento assíncrono. Sem guarda compartilhada, o sistema cria duas vendas — ou uma venda e um órfão financeiro. Eu, Tiago Montanha, tratei isso como bug de **dinheiro**, não de log.

## Problema

Race clássica:

1. Client retenta (timeout, double-click, gateway lento).
2. Webhook `charge.created` (ou equivalente) chega **antes** do `transaction_id` persistir — janela observada na ordem de **dezenas de segundos** em assinatura + cupom.
3. Segundo writer não encontra a venda e cria outra, às vezes com **valor do cupom** em vez do total.

Janela curta demais (ordem de 10s) falhava em checkout lento. Upsell paralelo e subscription sem `transaction_id` escapavam da chave ingênua. Resultado: estorno, chargeback, seller descrente.

## O que eu fiz

1. **Guarda durável na borda do pay** — middleware de idempotência. Chave derivada de identidade da tentativa (comprador + oferta + valor + meio + bucket de tempo), não de um ID que ainda não existe.
2. **Redis `SET NX` com TTL** — janela de **60s**. Trade-off explícito: compra legítima no 61º segundo pode passar; gateway &gt; 60s pode bloquear demais. 30s era pouco; 120s castigava retry honesto. ADR de uma página.
3. **Segundo guard no webhook** — para subscription, casar `payment_request_id` + tipo, não só `transaction_id` nulo.
4. **Bordas cobertas** — upsell paralelo (não colidir duas ofertas distintas), retry do gateway, ausência de `transaction_id`.
5. **Testes** — da ordem de **10** unitários de concorrência / chave / TTL. Sem teste, a janela volta a 10s no próximo “hotfix urgente”.

## Resultado / métricas

| Sinal | Rótulo |
| --- | --- |
| Classe “venda duplicada por race checkout/webhook” eliminada em produção após o deploy da guarda | **Resultado** |
| ~10 testes de idempotência no pacote do pay | **Resultado** |
| Queda de chamado de estorno/duplicata | **Qualitativo** — não publico volume financeiro |
| Janela 60s ótima para todo o catálogo | **Não afirmado** — é trade-off, não lei |

“Zero duplicata para sempre” seria mentira. Zero **dessa classe**, com os guards no caminho quente, é o claim honesto.

## Aprendizados Staff

- Idempotência é padrão transversal. Um middleware numa API não conserta o webhook da squad ao lado — por isso o segundo guard.
- A chave é o design. Hash demais e você bloqueia upsell; hash de menos e você duplica.
- Teste de corrida é documentação executável do ADR. O número 60 só existe se o teste o protege.
- Dinheiro duplicado é o tipo de bug que o Staff puxa mesmo quando “não é da minha squad”.

## Tags

`checkout` · `idempotencia` · `redis` · `webhook` · `race` · `pagamentos`
