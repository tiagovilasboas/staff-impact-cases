#!/usr/bin/env python3
"""Fail if a case file is missing the required Staff headings, in order."""

from __future__ import annotations

import os
import sys

REQUIRED = [
    "## Papel / período aproximado",
    "## Contexto",
    "## Problema",
    "## O que eu fiz",
    "## Resultado / métricas",
    "## Aprendizados Staff",
    "## Tags",
]

SKIP_NAMES = {"INDEX.md"}


def iter_case_files(cases_dir: str) -> list[str]:
    paths: list[str] = []
    for name in sorted(os.listdir(cases_dir)):
        if not name.endswith(".md") or name in SKIP_NAMES:
            continue
        paths.append(os.path.join(cases_dir, name))
    return paths


def missing_in_order(text: str) -> list[str]:
    missing: list[str] = []
    cursor = 0
    for heading in REQUIRED:
        idx = text.find(heading, cursor)
        if idx < 0:
            missing.append(heading)
            continue
        cursor = idx + len(heading)
    return missing


def main() -> int:
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    cases_dir = os.path.join(root, "cases")
    failures: list[str] = []
    checked = 0
    for path in iter_case_files(cases_dir):
        checked += 1
        text = open(path, encoding="utf-8").read()
        missing = missing_in_order(text)
        if missing:
            rel = os.path.relpath(path, root)
            failures.append(f"{rel}: missing or out of order {missing}")
    if checked == 0:
        print("Case headings: no case files found")
        return 1
    if failures:
        print("Case headings:")
        for item in failures:
            print(f"  {item}")
        return 1
    print(f"Case headings: ok ({checked} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
