# Observabilidade frontend: de ~900 catches silenciosos a Sentry em quatro fronts

**Papel.** Driver do padrão (autor do chapter); consultor das squads de FE - quatro fronts, leverage de várias squads. **Antes.** Browser cego; ~900 catches silenciosos; PIX e upload no mesmo saco. **Depois.** Sentry em quatro projetos; tags de domínio; PII masking. **Decisão.** SDK só em produção + sampling conservador + chapter; recusei só APM e sampling 100%. **Não medido neste texto.** crash-free, “60% dos bugs”, MTTR final.

## Papel / período aproximado

Staff / Tech Lead de sustentação, marketplace de creators e checkout de alto volume. Período aproximado: 2026.

## Contexto

Quatro frontends (checkout, dois painéis de seller, shell de admin) em React/Vue, sem telemetria de browser. Infra e API já tinham métricas. O navegador - onde o botão pagar vive - era ponto cego. Eu, Tiago Montanha, tratei isso como gap de receita, não como “mais uma ferramenta”.

**Restrição.** Quatro repos, squads distintas, sem dono de erro de client. LGPD: e-mail, documento e token não podem ir para o vendor. Quota: sampling alto queima orçamento e vira ruído. Calendário de checkout não parava para um “projeto de observabilidade”. Complementar Grafana/APM, não substituir.

## Problema

Contei da ordem de **~900** `catch` vazios ou logs que engoliam a exceção. Seller e comprador falhavam sem stack, sem release, sem rota. Sustentação descobria pelo ticket, dias depois. Sem tag de domínio, um erro de PIX misturava com um erro de upload. Sem máscara, qualquer SDK virava risco LGPD.

O custo invisível: HTTP 200 no BFF de pagamentos e TypeError no client. Conversão que some sem alarme. O irmão operacional (push morto por semanas) está em [falha-silenciosa-notificacoes.md](falha-silenciosa-notificacoes.md) - mesma classe, outro canal.

| Dimensão | Antes (observado) |
| --- | --- |
| Telemetria de browser | Quase zero; só ticket |
| `catch` vazio / log que engole | ~900 (contagem estática) |
| Contexto na issue | Sem release, rota, domínio ou fluxo |
| PII no payload de erro | Risco aberto se ligasse um SDK cru |
| Dono do alerta | Ninguém; volume misturado |

## O que eu fiz

**Decisão.** Aceitei SDK só em produção, sampling conservador, tags de domínio como contrato e chapter como produto. Recusei: só APM (não vê TypeError no botão), sampling 100% (custo + ruído), `captureException` nu (sem dono), big bang nos quatro repos no mesmo dia, session replay sempre ligado.

1. **Mapa de risco por frontend** - rotas de dinheiro e de jornada do seller primeiro; resto depois.
2. **SDK em produção apenas**, sampling conservador, source maps no release. Padrão extraído no próprio init: sampling, PII, tags - sem SDK cru.
3. **Tags de domínio e fluxo** (`domain`, `flow`, faixa de valor sem PII) via `withScope` - nunca `captureException` nu.
4. **PII masking** em `beforeSend`, `sendDefaultPii: false`. E-mail, documento, token: fora.
5. **Chapter de frontend** - um guia, quatro mapas, ownership por repo. Enablement: o padrão sobrevive à minha agenda.
6. Complemento a Grafana/APM, não substituição. Cada camada responde uma pergunta diferente.
7. **Evidência no rito** - issue com release + breadcrumb vira input de postmortem, não lore. Molde: timeline, evidência, ação com dono.

## Resultado / métricas

| Sinal | Antes | Depois | Rótulo |
| --- | --- | --- | --- |
| Catches silenciosos no client | ~900 (contagem estática) | Instrumentados; erro vira issue com release | **Resultado** (contagem + adoção) |
| Visibilidade de erro de browser | Quase zero | Quatro projetos; contexto de jornada | **Resultado** |
| Tag `domain` / `flow` | Ausente | Contrato no `withScope` | **Resultado** |
| PII no SDK | Risco se ligasse cru | `beforeSend` + `sendDefaultPii: false` | **Resultado** |
| Adoção | Proposta + POC | Plataforma escolhida para FE | **Resultado** |
| Latência de detecção | Ordem de **meses** no caso irmão (push morto) | **Meta:** &lt;24h com alerta + dashboard | meta |
| Taxa de incidente de integração / mês | Baseline alta (ordem de dezena) | **Alvo:** cair a um dígito baixo | alvo - não afirmo final auditado |
| MTTR de bug de checkout no client | Horas (reprodução cega) | **Alvo:** dezenas de minutos com breadcrumb + source map | alvo |

Números de “60% dos bugs antes do suporte” ou “crash-free 99,5%” são **metas de mercado / OKR**, não um before/after que eu publique como medido neste texto.

## Aprendizados Staff

- Observabilidade de frontend é leverage: um padrão × quatro repos × cinco squads.
- Tag de domínio é contrato social - sem ela o volume vira ruído e ninguém dono.
- Enablement (chapter, guia, mapa) vale mais que o PR do SDK. O SDK sem dono vira quota queimada.
- Separe **proposta** de **produção**. Eu vendi o gap; o time adotou; a meta de latência continua meta até o trimestre fechar o número.
- Kit público não prova que estes rates rodaram numa marca. Prova o padrão que eu extraí.

## Tags

`observabilidade` · `sentry` · `frontend` · `pii` · `chapter` · `staff-leverage`
