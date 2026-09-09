# Contribuindo

Este repositório é um **portfólio público de cases Staff** em PT-BR. Não é um log de incidentes reais com IDs, nem um dump de wiki corporativa.

Leia [AGENTS.md](AGENTS.md) antes de editar. Abra PR contra `main` - não commite direto.

## O que cabe aqui

- Narrativa densa em primeira pessoa, empregador genérico, métrica honesta.
- Ajuste de clareza, tags, ou de um **resultado** vs **meta** mal rotulado.
- Link de inspiração em [docs/inspiracao.md](docs/inspiracao.md) - sem copiar texto de terceiros.

## O que não cabe

- Nome de empresa, produto comercial, ticket interno, DSN, hostname, e-mail de seller.
- Seção `Purpose` / `Propósito` no README.
- Expandir `AGENTS.md` além de 80 linhas.

## Como editar um case

1. Um arquivo em `cases/`. Atualize [cases/INDEX.md](cases/INDEX.md) e [llms.txt](llms.txt).
2. Estrutura fixa (PT): título SEO · papel/período · contexto · problema · o que eu fiz · resultado/métricas · aprendizados Staff · tags.
3. Rode:

```bash
python3 scripts/check-anonymization.py
python3 scripts/check-md-links.py
npx --yes markdownlint-cli2@0.23.2 "**/*.md"
test "$(wc -l < AGENTS.md)" -le 80
```

Contribuições sob [MIT](LICENSE).
