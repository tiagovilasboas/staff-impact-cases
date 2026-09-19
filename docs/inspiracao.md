# Inspiração - como ler cases (os dos outros e os meus)

Eu, Tiago Montanha, sou **apaixonado por estudar cases** de engenharia e frontend como ofício: decisão, trade-off, evidência, leverage. Ler bem um case alheio é treino Staff; escrever o meu sem vazar IP é o outro lado da mesma disciplina.

O score mora em [docs/case-rubric.md](case-rubric.md). Calibração: [exemplo pontuado (~8.5)](case-rubric.md#worked-example-observabilidade-frontend). Aqui está a curadoria (não é autoria minha). Não copio os textos; extraio o craft.

## Craft de promo packet (o que eu extraio)

| Craft | O que entra neste INDEX |
| --- | --- |
| Projeto Staff | O que eu fiz, impacto com meta clara, o que tornou complexo. Impacto quantificável quando existir. Glue work conta. |
| Frase de impacto | Iniciativa → impacto de negócio → meu papel / accountability → quantos times. |
| Leverage organizacional | Before/after, inclusive contrafactual (crise que não aconteceu). Não é lista de PRs pessoais. |
| Evidência e risco | ADR/RFC/postmortem como artefato (aqui: o próprio case). Papel **autor / driver / consultor**. Rollback visível. |

Fontes (link only):

- [Promotion packets (staffeng)](https://staffeng.com/guides/promo-packets/)
- [Phrasing your impact in promotion packets](https://medium.com/staff-engineering-learnings/phrasing-your-impact-in-promotion-packets-441e6ae73552)
- [Staff engineer accomplishments](https://www.getprov.app/blog/examples/staff-engineer-accomplishments/)
- [Staff engineer promotion portfolio](https://heyytechy.com/staff-engineer-promotion-portfolio-github-pages/)

## Leitura de cases de frontend (não é autoria minha)

- [andrew--r/frontend-case-studies](https://github.com/andrew--r/frontend-case-studies) - curadoria pública de estudos de caso de frontend da indústria. **Inspiração e leitura.** Não afirmo que essas histórias sejam minhas. Não copio o conteúdo daquele repositório; o link basta.

## Como ler um case externo

1. Separe **contexto da empresa** de **padrão transferível** (BFF, sampling, idempotência, kill-switch).
2. Pergunte qual métrica é medida e qual é narrativa de marketing.
3. Anote o trade-off que o autor aceitou - é aí que o Staff aparece.
4. Não replique marca, volume financeiro ou detalhe de produto no *seu* texto público.

## Como ler os cases deste repo

Aqui o contrato é o inverso do catálogo externo:

| Este repo | Catálogo externo |
| --- | --- |
| Primeira pessoa, autoria provada | Terceiros; eu só indico a leitura |
| Empregadores anonimizados | Muitas vezes nomeiam a empresa |
| Métrica rotulada (resultado vs meta) | Qualidade varia; leia com ceticismo |
| Sem IP confidencial | Respeite a licença de cada fonte |

Volte ao mapa: [cases/INDEX.md](../cases/INDEX.md).
