# BFF GraphQL: dezenas de REST no client limitado viram uma query por tela

**Papel.** Autor do BFF; driver para destravar o front frente ao legado. **Antes.** Dezenas de REST no device limitado; front espera o monolito. **Depois.** Uma query por tela; DataLoader no servidor; cache só de catálogo. **Decisão.** GraphQL BFF + DataLoader; recusei waterfall no device e federação. **Não medido neste texto.** RUM em ms e % de bytes da época.

## Papel / período aproximado

Tech Lead / engenheiro sênior em **plataforma OTT**. Clientes: Smart TVs antigas e mobile em rede ruim. Período aproximado: 2019-2021.

## Contexto

A tela montava o catálogo no device: dezenas de REST sequenciais, payload gordo (overfetch), ida-e-volta demais (underfetch). CPU e RAM de TV de 2015 não perdoam. Eu, Tiago Montanha, tirei a orquestração do client.

**Restrição.** Catálogo no ar todos os dias; não havia janela para reescrever o monolito. Device de ~2015: orçamento de CPU, RAM e rede 3G. Time de produto não podia esperar o ciclo do legado para cada tela nova. BFF não podia virar segundo monolito. Cache de catálogo não mistura com sessão.

## Problema

Dor de negócio: tela que não abre, abandono na home, sprint de backend para cada card novo. O client limitado pagava a conta da orquestração que deveria ser do servidor.

| Dimensão | Antes (observado) |
| --- | --- |
| Chamadas no device por tela | Dezenas de REST em cascata |
| Payload | Overfetch: campos que a TV não renderiza |
| Waterfall | Underfetch: N+1 no JavaScript do device |
| Acoplamento | Client preso a APIs legadas |
| Autonomia de deploy | Front espera o monolito |

O irmão de superfície (BFF como perímetro, não como proxy inocente) está em [appsec-bff-go-live.md](appsec-bff-go-live.md). Aqui o problema é física de rede e de device, não ASVS.

## O que eu fiz

**Decisão.** Aceitei BFF Node + GraphQL com uma query por tela, DataLoader no servidor e cache só de catálogo. Recusei: deixar o waterfall no device (física), BFF REST 1:1 (ainda N idas), GraphQL sem DataLoader (N+1 com sintaxe nova), federação ou mesh (sobrepeso para o momento), reescrever o monolito antes de destravar o front.

1. **BFF em Node com GraphQL** - schema sob medida para TV/mobile; uma query por tela.
2. **DataLoader** para colapsar N+1 no servidor, não no JavaScript da TV.
3. **Cache** Redis + CDN no que é catálogo, nunca no que é sessão ou perfil.
4. **Contrato no BFF** - front evolui schema sem wait de deploy do legado.
5. **Evidência** - mapa tela → query; resolvers com batch visível; cache hit no catálogo vs miss forçado em sessão. Sem RUM público neste texto.

## Resultado / métricas

| Sinal | Antes | Depois | Rótulo |
| --- | --- | --- | --- |
| Ida à rede no device por tela | Dezenas de REST | Uma ida ao BFF | **Resultado** (arquitetura) |
| Orquestração | JavaScript no device limitado | Servidor (DataLoader) | **Resultado** |
| Cache | Ausente ou misturado | Catálogo no Redis/CDN; sessão fora | **Resultado** |
| Autonomia de deploy do front vs legado | Front espera o monolito | Contrato no BFF | **Resultado** organizacional |
| CPU / rede no device | Alto (waterfall + overfetch) | Menor (qualitativo) | **Qualitativo** - não publico RUM da época |
| Latência de tela em ms | Desconhecida neste texto | **Não medido neste texto** | não afirmo número |

Números de “X ms na home” ou “Y% menos bytes” seriam **meta de RUM**, não um before/after que eu publique como medido neste texto.

## Aprendizados Staff

- Cliente limitado muda o lugar da orquestração. BFF não é moda; é física de rede.
- GraphQL sem DataLoader é N+1 com sintaxe nova.
- O ganho político (front desacoplado) às vezes paga mais que o ms. Escreva os dois.
- BFF que orquestra catálogo ainda é perímetro. O case de AppSec é o complemento, não o substituto.

## Tags

`graphql` · `bff` · `ott` · `performance` · `client-limitado`
