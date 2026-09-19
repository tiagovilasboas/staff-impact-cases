# Contribuindo

Este repositório é um **INDEX público de cases Staff** em PT-BR. Evidência narrativa para recrutador: não é produto, não é CLI, não é hub de kits, não é log de incidentes com IDs, nem dump de wiki corporativa.

Leia [AGENTS.md](AGENTS.md) antes de editar. Abra PR contra `main` - não commite direto.

## O que cabe aqui

- Narrativa densa em primeira pessoa, empregador genérico, métrica honesta.
- Ajuste de clareza, tags, ou de um **resultado** vs **meta** mal rotulado.
- Link de inspiração em [docs/inspiracao.md](docs/inspiracao.md) - sem copiar texto de terceiros.
- Case novo = um arquivo + uma linha em [cases/INDEX.md](cases/INDEX.md) + uma linha no README + uma linha em [llms.txt](llms.txt).

## O que não cabe

- Nome de empresa, produto comercial, ticket interno, DSN, hostname, e-mail de seller.
- Seção `Purpose` / `Propósito` no README.
- Seção `## Related` com repositórios irmãos no README (este INDEX se lê sozinho).
- Emoldurar o repo como produto ou CLI.
- Expandir `AGENTS.md` além de 80 linhas.

## Como editar um case

1. Um arquivo em `cases/`. Atualize [cases/INDEX.md](cases/INDEX.md), [README.md](README.md) e [llms.txt](llms.txt).
2. Estrutura fixa (PT): título SEO · abertura num fôlego · papel/período · contexto · problema · o que eu fiz · resultado/métricas · aprendizados Staff · tags. Rubrica: [docs/case-rubric.md](docs/case-rubric.md). Calibre o score no [exemplo pontuado](docs/case-rubric.md#worked-example-observabilidade-frontend) (~8.5; não invente métrica para 9+).
3. Abertura com **Papel.** **Antes.** **Depois.** **Decisão.** e `Não medido`. Depois **Restrição.** no contexto. Tabela antes/depois em resultado. Papel no rito: autor, driver ou consultor.
4. Rode:

```bash
python3 scripts/check-anonymization.py
python3 scripts/check-md-links.py
python3 scripts/check-case-headings.py
python3 scripts/test_checks.py
npx --yes markdownlint-cli2@0.23.2 "**/*.md"
test "$(wc -l < AGENTS.md)" -le 80
```

Contribuições sob [MIT](LICENSE).
