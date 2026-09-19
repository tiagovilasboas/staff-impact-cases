#!/usr/bin/env python3
"""Fail if a case file is missing required headings, opening, or rubric markers."""

from __future__ import annotations

import os
import re
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

MARKERS = [
    "Restrição.",
    "Decisão.",
    "Eu, Tiago Montanha",
]

OPENING_MARKERS = [
    "**Papel.**",
    "**Antes.**",
    "**Depois.**",
    "**Decisão.**",
    "Não medido",
]

SKIP_NAMES = {"INDEX.md"}


def iter_case_files(cases_dir: str) -> list[str]:
    if not os.path.isdir(cases_dir):
        return []
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


def empty_required_sections(text: str) -> list[str]:
    empty: list[str] = []
    for index, heading in enumerate(REQUIRED):
        start = text.find(heading)
        if start < 0:
            continue
        body_start = start + len(heading)
        if index + 1 < len(REQUIRED):
            body_end = text.find(REQUIRED[index + 1], body_start)
            if body_end < 0:
                body_end = len(text)
        else:
            body_end = len(text)
        if not text[body_start:body_end].strip():
            empty.append(heading)
    return empty


def resultado_table_ok(text: str) -> bool:
    start = text.find("## Resultado / métricas")
    end = text.find("## Aprendizados Staff")
    if start < 0 or end < 0 or end <= start:
        return False
    section = text[start:end]
    return "|" in section and "Antes" in section and "Depois" in section


def tags_ok(text: str) -> bool:
    start = text.find("## Tags")
    if start < 0:
        return False
    return text[start:].count("`") >= 2


def scan(root: str) -> list[str]:
    cases_dir = os.path.join(root, "cases")
    failures: list[str] = []
    paths = iter_case_files(cases_dir)
    if not paths:
        return ["Case headings: no case files found"]
    for path in paths:
        text = open(path, encoding="utf-8").read()
        rel = os.path.relpath(path, root)
        if not re.search(r"^# ", text, flags=re.M):
            failures.append(f"{rel}: missing H1 title")
        missing = missing_in_order(text)
        if missing:
            failures.append(f"{rel}: missing or out of order {missing}")
        empty = empty_required_sections(text)
        if empty:
            failures.append(f"{rel}: empty sections {empty}")
        for marker in MARKERS:
            if marker not in text:
                failures.append(f"{rel}: missing {marker!r}")
        cut = text.find("## Problema")
        head = text[:cut] if cut >= 0 else text
        for marker in OPENING_MARKERS:
            if marker not in head:
                failures.append(f"{rel}: opening before Problema missing {marker!r}")
        if not resultado_table_ok(text):
            failures.append(f"{rel}: Resultado must have a table with Antes and Depois")
        if not tags_ok(text):
            failures.append(f"{rel}: Tags must list at least one `tag`")
    return failures


def main() -> int:
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    failures = scan(root)
    checked = len(iter_case_files(os.path.join(root, "cases")))
    if failures:
        print("Case headings:")
        for item in failures:
            print(f"  {item}")
        return 1
    print(f"Case headings: ok ({checked} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
