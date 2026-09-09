# BFF GraphQL: dezenas de REST no client limitado

## Papel / período aproximado

Tech Lead / engenheiro sênior em **plataforma OTT**. Clientes: Smart TVs antigas e mobile em rede ruim. Período aproximado: 2019–2021.

## Contexto

A tela montava o catálogo no device: dezenas de REST sequenciais, payload gordo (overfetch), ida-e-volta demais (underfetch). CPU e RAM de TV de 2015 não perdoam. Eu, Tiago Montanha, tirei a orquestração do client.

## Problema

- Client acoplado a APIs legadas — cada tela nova pedia sprint de backend.
- Overfetch: campos que a TV não renderiza viajam na rede 3G.
- Underfetch: waterfall de N+1 no JavaScript do device.
- Time de produto preso ao ciclo do monolito.

## O que eu fiz

1. **BFF em Node** com **GraphQL** — uma query por tela; schema sob medida para TV/mobile.
2. **DataLoader** para colapsar N+1 no servidor.
3. Cache (Redis + CDN) no que é catálogo, não no que é sessão.
4. Front evolui schema sem wait de deploy do legado — contrato no BFF.

Case curto de propósito: o leverage é o desenho, não o inventário de resolvers.

## Resultado / métricas

| Sinal | Rótulo |
| --- | --- |
| Dezenas de REST no client → **uma** ida ao BFF por tela | **Resultado** de arquitetura |
| Menos CPU/rede no device limitado | **Qualitativo** — não publico RUM da época |
| Autonomia de deploy do front vs legado | **Resultado** organizacional |
| Latência de tela em X ms | **Não medido neste texto** |

## Aprendizados Staff

- Cliente limitado muda o lugar da orquestração. BFF não é moda; é física de rede.
- GraphQL sem DataLoader é N+1 com sintaxe nova.
- O ganho político (front desacoplado) às vezes paga mais que o ms. Escreva os dois.

## Tags

`graphql` · `bff` · `ott` · `performance` · `client-limitado`
