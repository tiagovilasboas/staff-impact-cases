# AppSec no BFF: auditoria estilo ASVS-L2 que bloqueou um go-live inseguro

## Papel / período aproximado

Staff com AppSec aplicada (curso de defesa cibernética em paralelo). Período aproximado: 2025-2026. Superfície: **BFF de pagamentos** na frente de um checkout de alto volume.

## Contexto

O BFF ia a produção como “só um aggregador”. Na prática ele autentica, agrega dados de seller/comprador e fala com o gateway. Go-live sem barra de segurança é go-live de superfície de ataque. Eu, Tiago Montanha, tratei o BFF como aplicação ASVS - não como proxy inocente.

## Problema

Revisão estilo [OWASP ASVS L2](https://owasp.org/www-project-application-security-verification-standard/) (verificação para apps que movem dinheiro / PII), sem inventar um selo formal da organização:

| Achado | Risco |
| --- | --- |
| Bearer mal usado (token em query, header opcional, ou “confia no BFF” sem validar escopo) | Roubo de sessão, replay |
| IDOR - recurso por ID sem checar dono (seller A lê seller B) | Vazamento financeiro / LGPD |
| CORS `*` com credenciais ou origem reflexiva | Exfiltração do browser |
| Superfície admin no mesmo host sem allowlist | Privilégio lateral |

Nenhum desses achados precisa de exploit público neste repo. O ponto Staff é o **mapeamento** e a decisão de não ir ao ar.

## O que eu fiz

1. **Checklist L2 enxuto** - autenticação, sessão, controle de acesso, CORS, headers, logs sem segredo. Uma página, não um PDF de 200 itens.
2. **Mapeamento achado → controle** - cada item com severidade, evidência (teste), dono, e “bloqueia go-live? sim/não”.
3. **Auth endurecida** - bearer só em `Authorization`; validação de issuer/audience/exp; recusar token no query string.
4. **Autorização no BFF** - toda leitura/escrita de recurso financeiro checa `subject === owner` (ou papel explícito). Teste de IDOR negativo no CI.
5. **CORS allowlist** - origens do checkout e do admin; sem coringa em ambiente com cookie/credencial.
6. **Bloqueio do go-live** até os itens “bloqueia = sim” fecharem. Pressão de calendário não vira aceite.
7. **Testes de evidência** - contrato de header; origem recusada; IDOR 403; snapshot de headers de segurança.

## Resultado / métricas

| Sinal | Rótulo |
| --- | --- |
| Go-live adiado até auth + CORS + IDOR fecharem | **Resultado** - a decisão foi minha a defender |
| Testes de regressão nos três achados no pipeline | **Resultado** |
| “Zero achado L2” como scorecard permanente | **Meta** - L2 é barra contínua, não um checklist de um dia |
| Redução de incidente de autorização em produção | **Alvo** - não publico taxa aqui |

Não invento CVE, não publico payload, não cito host interno.

## Aprendizados Staff

- BFF **é** o perímetro. Quem chama “só frontend” no BFF de pagamentos está terceirizando o IDOR.
- Bloquear go-live é ato político-técnico. Documente o achado em linguagem de risco de negócio (dinheiro, PII), não só de header.
- Evidência = teste que falha se alguém reabrir o coringa. Review sem teste morre no próximo hotfix.
- AppSec no Staff não é “o time de segurança depois”. É gate na mesma PR que o feature.

## Tags

`appsec` · `asvs` · `bff` · `idor` · `cors` · `go-live`
