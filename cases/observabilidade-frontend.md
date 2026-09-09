# Observabilidade frontend: de ~900 catches silenciosos a Sentry em quatro fronts

## Papel / período aproximado

Staff / Tech Lead de sustentação, marketplace de creators e checkout de alto volume. Período aproximado: 2026.

## Contexto

Quatro frontends (checkout, dois painéis de seller, shell de admin) em React/Vue, sem telemetria de browser. Infra e API já tinham métricas. O navegador - onde o botão pagar vive - era ponto cego. Eu, Tiago Montanha, tratei isso como gap de receita, não como “mais uma ferramenta”.

## Problema

Contei da ordem de **~900** `catch` vazios ou logs que engoliam a exceção. Seller e comprador falhavam sem stack, sem release, sem rota. Sustentação descobria pelo ticket, dias depois. Sem tag de domínio, um erro de PIX misturava com um erro de upload. Sem máscara, qualquer SDK virava risco LGPD.

O custo invisível: HTTP 200 no BFF de pagamentos e TypeError no client. Conversão que some sem alarme.

## O que eu fiz

1. **Mapa de risco por frontend** - rotas de dinheiro e de jornada do seller primeiro; resto depois.
2. **SDK em produção apenas**, sampling conservador, source maps no release. Padrão que depois abri em [sentry-golden-path](https://github.com/tiagovilasboas/sentry-golden-path).
3. **Tags de domínio e fluxo** (`domain`, `flow`, faixa de valor sem PII) via `withScope` - nunca `captureException` nu.
4. **PII masking** em `beforeSend`, `sendDefaultPii: false`. E-mail, documento, token: fora.
5. **Chapter de frontend** - um guia, quatro mapas, ownership por repo. Enablement: o padrão sobrevive à minha agenda.
6. Complemento a Grafana/APM, não substituição. Cada camada responde uma pergunta diferente.

## Resultado / métricas

| Sinal | Antes | Depois / rótulo |
| --- | --- | --- |
| Catches silenciosos no client | ~900 (contagem estática) | Instrumentados; erro vira issue com release |
| Visibilidade de erro de browser | Quase zero | Quatro projetos; contexto de jornada |
| Adoção | Proposta + POC | Plataforma escolhida para FE (**resultado**) |
| Latência de detecção | Ordem de **meses** num caso irmão (push morto) | **Meta:** &lt;24h com alerta + dashboard |
| Taxa de incidente de integração / mês | Baseline alta (ordem de dezena) | **Alvo:** cair a um dígito baixo - não afirmo final auditado aqui |
| MTTR de bug de checkout no client | Horas (reprodução cega) | **Alvo:** dezenas de minutos com breadcrumb + source map |

Números de “60% dos bugs antes do suporte” ou “crash-free 99,5%” são **metas de mercado / OKR**, não um before/after que eu publique como medido neste texto.

## Aprendizados Staff

- Observabilidade de frontend é leverage: um padrão × quatro repos × cinco squads.
- Tag de domínio é contrato social - sem ela o volume vira ruído e ninguém dono.
- Enablement (chapter, guia, mapa) vale mais que o PR do SDK. O SDK sem dono vira quota queimada.
- Separe **proposta** de **produção**. Eu vendi o gap; o time adotou; a meta de latência continua meta até o trimestre fechar o número.

## Tags

`observabilidade` · `sentry` · `frontend` · `pii` · `chapter` · `staff-leverage`
