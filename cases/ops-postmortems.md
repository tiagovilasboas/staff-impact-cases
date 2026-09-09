# Ops N3: dashboard diário e cultura blameless de postmortem

## Papel / período aproximado

Tech Lead / Staff de sustentação N3 - última linha antes do seller. Marketplace de creators. Período aproximado: 2026 (~primeiro trimestre de operação na cadeira).

## Contexto

A squad via incidente pelo chamado. Sem ritual de aprendizagem, o mesmo padrão voltava: webhook, race, integração muda e ninguém alerta. Onboarding era lore. Eu, Tiago Montanha, precisava de um **sistema operacional** - não de heroísmo noturno.

## Problema

- Sem painel único do dia: CPU verde, seller vermelho.
- Postmortem informal (“a gente já sabe”) = conhecimento que viaja com a pessoa.
- Zero escrita estruturada no trimestre anterior.
- Dev novo gastava semana atrás de acesso e de “por onde começa”.

N3 sem telemetria de produto vira fila de ticket. N3 com dashboard e postmortem vira alavanca da plataforma.

## O que eu fiz

1. **Dashboard Grafana no estilo N3** - seções para integrações, filas, webhooks, jobs, saúde de push/e-mail. Uso **diário**, não slide de QBR. Versão iterada dezenas de vezes com o time.
2. **Rito blameless** - template no espírito SRE: timeline, causa primária vs latente, evidência, ação com dono e urgência. Sem nome para punir. O kit público está em [staff-postmortem](https://github.com/tiagovilasboas/staff-postmortem).
3. **Cadência** - incidente que dói seller ou dinheiro → escrita. Spike sem impacto de usuário não vira novela (gate de severidade).
4. **Onboarding** - lista curta: acessos, ambientes, o dashboard, os três postmortems que ensinam o domínio. Meta informal: produzir em menos de uma semana, não em um mês de sombra.
5. **Padrões sistêmicos** - extraí classes (falha silenciosa, race de webhook, lib deprecada, fix parcial em fluxo longo) e tratei como backlog de *guard rail*, não como 15 bugs isolados.

## Resultado / métricas

| Sinal | Número | Rótulo |
| --- | --- | --- |
| Postmortems publicados | **~15 em ~2 meses** | **Resultado** (contagem de escritos) |
| Dashboard em uso diário pelo N3 | sim | **Resultado** qualitativo |
| Detecção do caso de push morto | via painel, não só via ticket | **Resultado** (ver [falha-silenciosa-notificacoes.md](falha-silenciosa-notificacoes.md)) |
| Tempo até o primeiro PR útil de um recém-chegado | **Alvo:** &lt; 1 semana com o pacote de onboarding | meta operacional |
| Recorrência da mesma classe de incidente | **Alvo:** cair após o guard rail, não após o hotfix | não afirmo zero eterno |

Quinze textos não são vaidade. São onboarding empacotado e memória institucional.

## Aprendizados Staff

- Cultura blameless é infraestrutura. Sem ela o dashboard vira caça às bruxas e o time esconde sinal.
- Escrever 15 vezes o mesmo molde ensina o time a pensar em evidência. O template é o produto; o incidente é o input.
- Leverage de onboarding: um dashboard + três PMs escolhidos &gt; um tour de duas horas que ninguém grava.
- Staff não “faz o postmortem pelo time”. Staff faz o time não conseguir mais fechar o incidente sem o rito.

## Tags

`ops` · `grafana` · `postmortem` · `blameless` · `onboarding` · `n3`
