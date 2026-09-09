# Agents

Corpus de **cases de impacto Staff** em PT-BR, primeira pessoa, empregadores anonimizados. Humanos: [CONTRIBUTING.md](CONTRIBUTING.md).

## Layout

```text
cases/INDEX.md                         mapa de leitura
cases/*.md                             um case por arquivo
docs/inspiracao.md                     leitura externa (link only)
docs/case-rubric.md                    problem / constraint / decision / evidence / outcome
scripts/check-anonymization.py         CI: nomes/IDs proibidos
scripts/check-md-links.py              CI: links relativos
scripts/check-case-headings.py         CI: H2 obrigatórios em cases/
```

README é mapa. Sem `## Purpose` / `## Propósito`. `AGENTS.md` ≤ 80 linhas.

## Do

- Escreva em **português do Brasil**, primeira pessoa (“Eu, Tiago Montanha…”).
- Use rótulos genéricos: marketplace de creators, checkout de alto volume, BFF de pagamentos, plataforma OTT.
- Separe **resultado observado** de **meta/alvo**. Se o número não for final medido, rotule `meta` ou `alvo`.
- Arredonde métricas. Prefira ordem de grandeza a precisão falsa.
- Mantenha autoria: Maintainer Tiago Montanha · Staff · `@tiagovilasboas`.

## Don't

- Não invente nomes de empregador. Não use marcas da lista em `scripts/check-anonymization.py`.
- Não cole IDs de ticket, DSN, hostname interno, e-mail de seller, URL de wiki/ADO privado, número de PR privado.
- Não copie o conteúdo de [frontend-case-studies](https://github.com/andrew--r/frontend-case-studies); só o link.
- Não use em dash (U+2014). Prefira vírgula, ponto, hífen `-` ou parênteses.
- Não commite em `main`. Abra PR.

Verificar:

```bash
test "$(wc -l < AGENTS.md)" -le 80
python3 scripts/check-anonymization.py
python3 scripts/check-md-links.py
python3 scripts/check-case-headings.py
```
