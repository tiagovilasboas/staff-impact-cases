#!/usr/bin/env python3
"""Fail if a forbidden employer / ticket / secret pattern appears in the corpus."""

from __future__ import annotations

import os
import re
import sys

# Public portfolio: never leak employers, ticket IDs, private hosts, or DSNs.
FORBIDDEN = [
    (r"\bCogna\b", "employer"),
    (r"\bVoomp\b", "employer"),
    (r"\bGreenn\b", "employer"),
    (r"\bHotmart\b", "employer"),
    (r"\bGlobo(?:play|sat)?\b", "employer"),
    (r"\bCartola\b", "employer"),
    (r"Dell\s*Anno", "employer"),
    (r"Pagar\.?me", "vendor"),
    (r"\bOneSignal\b", "vendor"),
    (r"\bKiro\b", "product"),
    (r"\bVSUS-\d+", "ticket"),
    (r"\bVMPG-\d+", "ticket"),
    (r"\bVADM-\d+", "ticket"),
    (r"\bVGAT-\d+", "ticket"),
    (r"\bVPLY-\d+", "ticket"),
    (r"\bAB#\d+", "ticket"),
    (r"dev\.azure\.com", "private-host"),
    (r"atlassian\.net", "private-host"),
    (r"visualstudio\.com", "private-host"),
    (r"confluence\.", "private-host"),
    (r"sharepoint\.com", "private-host"),
    (r"\b[\w-]+\.internal\b", "private-host"),
    (r"ingest\.sentry\.io/[A-Za-z0-9]+", "dsn"),
    (r"\bSENTRY_DSN\b", "dsn"),
    (r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", "email"),
    (r"\bWendell\b", "seller"),
]

SKIP_DIRS = {".git", "node_modules", "scripts"}
SKIP_FILES = {"check-anonymization.py"}
TEXT_SUFFIXES = (".md", ".txt", ".yml", ".yaml", ".jsonc")


def iter_text_files(root: str) -> list[str]:
    paths: list[str] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if name in SKIP_FILES:
                continue
            if name.endswith(TEXT_SUFFIXES):
                paths.append(os.path.join(dirpath, name))
    return paths


def scan(root: str) -> list[str]:
    if not FORBIDDEN:
        return ["FORBIDDEN list is empty"]
    hits: list[str] = []
    files = iter_text_files(root)
    if not files:
        return ["no text files found to scan"]
    for path in files:
        text = open(path, encoding="utf-8").read()
        rel = os.path.relpath(path, root)
        if "\u2014" in text:
            hits.append(f"{rel}: typography em-dash U+2014")
        for pattern, kind in FORBIDDEN:
            for match in re.finditer(pattern, text, flags=re.IGNORECASE):
                hits.append(f"{rel}: {kind} '{match.group(0)}'")
    return hits


def main() -> int:
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    hits = scan(root)
    if hits:
        print("Anonymization leaks:")
        for item in hits:
            print(f"  {item}")
        return 1
    print("Anonymization: ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
