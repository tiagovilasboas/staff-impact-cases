#!/usr/bin/env python3
"""Regression: broken fixtures must fail; the live corpus must pass."""

from __future__ import annotations

import importlib.util
import os
import sys
import tempfile
from types import ModuleType

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(SCRIPTS, ".."))


def load(filename: str) -> ModuleType:
    path = os.path.join(SCRIPTS, filename)
    spec = importlib.util.spec_from_file_location(filename, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write(root: str, rel: str, content: str) -> None:
    path = os.path.join(root, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(content)


def require(cond: bool, message: str, failures: list[str]) -> None:
    if not cond:
        failures.append(message)


def expect_hit(hits: list[str], needle: str, label: str, failures: list[str]) -> None:
    if not any(needle in item for item in hits):
        failures.append(f"{label}: expected a hit containing {needle!r}, got {hits}")


THIN_CASE = """# Thin

## Papel / período aproximado
Staff.

## Contexto
Texto.

## Problema
Dor.

## O que eu fiz
Ação.

## Resultado / métricas
Qualitativo.

## Aprendizados Staff
Nota.

## Tags
`ops`
"""


def main() -> int:
    anon = load("check-anonymization.py")
    heads = load("check-case-headings.py")
    links = load("check-md-links.py")
    failures: list[str] = []

    forbidden = getattr(anon, "FORBIDDEN")
    require(len(forbidden) >= 10, "FORBIDDEN shrank below a useful floor", failures)
    require(any("Cogna" in pattern for pattern, _kind in forbidden), "Cogna dropped from FORBIDDEN", failures)
    require(len(getattr(heads, "REQUIRED")) == 7, "REQUIRED headings changed count", failures)

    live_anon = anon.scan(ROOT)
    live_heads = heads.scan(ROOT)
    live_links = links.scan(ROOT)
    require(live_anon == [], f"live corpus anonymization should pass: {live_anon}", failures)
    require(live_heads == [], f"live corpus headings should pass: {live_heads}", failures)
    require(live_links == [], f"live corpus links should pass: {live_links}", failures)

    with tempfile.TemporaryDirectory() as tmp:
        write(tmp, "README.md", "## Related\n\nSee [missing](nope.md) and https://github.com/tiagovilasboas/sentry-golden-path\n")
        write(tmp, "llms.txt", "no cases\n")
        write(tmp, "cases/INDEX.md", "empty\n")
        write(tmp, "cases/orphan.md", THIN_CASE)
        write(tmp, "cases/leaky.md", "Employer Cogna and email seller@example.com — leak.\n")

        expect_hit(anon.scan(tmp), "employer", "Cogna fixture", failures)
        expect_hit(anon.scan(tmp), "email", "email fixture", failures)
        expect_hit(anon.scan(tmp), "em-dash", "em-dash fixture", failures)
        expect_hit(heads.scan(tmp), "Restrição.", "thin case missing constraint", failures)
        expect_hit(heads.scan(tmp), "Antes and Depois", "thin case missing before/after", failures)
        expect_hit(links.scan(tmp), "sibling-hub", "sibling URL fixture", failures)
        expect_hit(links.scan(tmp), "## Related", "Related heading fixture", failures)
        expect_hit(links.scan(tmp), "nope.md", "broken relative link", failures)
        expect_hit(links.scan(tmp), "missing case links", "INDEX drift", failures)

    if failures:
        print("test_checks: FAIL")
        for item in failures:
            print(f"  {item}")
        return 1
    print("test_checks: ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
