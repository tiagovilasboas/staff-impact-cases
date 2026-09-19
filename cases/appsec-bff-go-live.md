# AppSec no BFF: auditoria estilo ASVS-L2 que bloqueou um go-live inseguro

**Papel.** Driver do gate de go-live; autor do checklist L2 no BFF de pagamentos. **Antes.** Bearer frouxo, IDOR, CORS coringa; o calendário mandava ir. **Depois.** Go-live adiado até auth + CORS + IDOR fecharem; testes no pipeline. **Decisão.** Bloquear o ar; recusei ship-and-patch. **Não medido neste texto.** taxa de incidente de autorização; “zero achado L2” permanente. Contrafactual: superfície insegura que não foi a produção.

## Papel / período aproximado

Staff com AppSec aplicada (curso de defesa cibernética em paralelo). Período aproximado: 2025-2026. Superfície: **BFF de pagamentos** na frente de um checkout de alto volume.

## Contexto

O BFF ia a produção como “só um aggregador”. Na prática ele autentica, agrega dados de seller/comprador e fala com o gateway. Go-live sem barra de segurança é go-live de superfície de ataque. Eu, Tiago Montanha, tratei o BFF como aplicação ASVS - não como proxy inocente.

**Restrição.** Calendário de go-live já vendido. Narrativa da casa: “é só frontend no meio”. Sem selo formal da organização (eu usei [OWASP ASVS L2](https://owasp.org/www-project-application-security-verification-standard/) como barra, não como certificado interno). Sem exploit público neste repo. Achado precisa de evidência (`path:line` ou teste que falha).

## Problema

Revisão estilo ASVS L2 (verificação para apps que movem dinheiro / PII), sem inventar um selo formal da organização:

| Achado | Antes (superfície) | Risco de negócio |
| --- | --- | --- |
| Bearer mal usado | Token em query, header opcional, ou “confia no BFF” sem escopo | Roubo de sessão, replay |
| IDOR | Recurso por ID sem checar dono (seller A lê seller B) | Vazamento financeiro / LGPD |
| CORS frouxo | `*` com credenciais ou origem reflexiva | Exfiltração do browser |
| Superfície admin | Mesmo host sem allowlist | Privilégio lateral |
| Log de auth | Risco de token / PII no log | Segredo no sink de observabilidade |

Nenhum desses achados precisa de exploit público neste repo. O ponto Staff é o **mapeamento** e a decisão de não ir ao ar.

## O que eu fiz

**Decisão.** Bloquear o go-live até auth, CORS e IDOR fecharem. Recusei: “ship and patch”, confiar no gateway para autorização, CORS coringa “só no staging”, review de segurança depois do feature. Pressão de calendário não vira aceite.

1. **Checklist L2 enxuto** - autenticação, sessão, controle de acesso, CORS, headers, logs sem segredo. Uma página, não um PDF de 200 itens.
2. **Mapeamento achado → controle** - cada item com severidade, evidência (teste ou `path:line`), dono, e “bloqueia go-live? sim/não”.
3. **Auth endurecida** - bearer só em `Authorization`; validação de issuer/audience/exp; recusar token no query string.
4. **Autorização no BFF** - toda leitura/escrita de recurso financeiro checa `subject === owner` (ou papel explícito). Teste de IDOR negativo no CI.
5. **CORS allowlist** - origens do checkout e do admin; sem coringa em ambiente com cookie/credencial.
6. **Logs sem segredo** - token e documento fora do sink; alinhado ao masking de PII do case de [observabilidade-frontend.md](observabilidade-frontend.md).
7. **Bloqueio do go-live** até os itens “bloqueia = sim” fecharem.
8. **Testes de evidência** - contrato de header; origem recusada; IDOR 403; snapshot de headers de segurança. Review sem teste morre no próximo hotfix.

## Resultado / métricas

| Sinal | Antes | Depois | Rótulo |
| --- | --- | --- | --- |
| Go-live | Calendário mandava ir | Adiado até auth + CORS + IDOR fecharem | **Resultado** (decisão defendida) |
| Bearer | Query / header opcional / escopo implícito | Só `Authorization`; iss/aud/exp | **Resultado** |
| IDOR em recurso financeiro | ID sem checagem de dono | `subject === owner` + teste 403 no CI | **Resultado** |
| CORS | Coringa ou origem reflexiva | Allowlist checkout + admin | **Resultado** |
| Superfície admin | Mesmo host sem allowlist | Allowlist / recorte de rota | **Resultado** |
| Regressão dos três achados | Review verbal | Testes no pipeline | **Resultado** |
| “Zero achado L2” permanente | - | Barra contínua, não um dia | **Meta** |
| Incidente de autorização em produção | Baseline não publicada | Queda sustentada | **Alvo** - não publico taxa |

Não invento CVE, não publico payload, não cito host interno.

## Aprendizados Staff

- BFF **é** o perímetro. Quem chama “só frontend” no BFF de pagamentos está terceirizando o IDOR.
- Bloquear go-live é ato político-técnico. Documente o achado em linguagem de risco de negócio (dinheiro, PII), não só de header.
- Evidência = teste que falha se alguém reabrir o coringa, ou `path:line`. Review sem teste morre no próximo hotfix.
- AppSec no Staff não é “o time de segurança depois”. É gate na mesma PR que o feature.
- Review sem `path:line` ou teste que falha não é gate. Este case é a decisão de calendário, não um produto de review.

## Tags

`appsec` · `asvs` · `bff` · `idor` · `cors` · `go-live`
