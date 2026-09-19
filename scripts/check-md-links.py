#!/usr/bin/env python3
"""Fail if a relative Markdown link does not exist, or the INDEX drifts."""

from __future__ import annotations

import os
import re
import sys

LINK = re.compile(r"\[([^\]]*)\]\(([^)]*)\)")
REF_DEF = re.compile(r"^\[([^\]]+)\]:\s+(\S+)", re.M)
SKIP_PREFIXES = ("http://", "https://", "mailto:")
SIBLING_URLS = (
    "github.com/tiagovilasboas/sentry-golden-path",
    "github.com/tiagovilasboas/agentic-code-review",
    "github.com/tiagovilasboas/staff-postmortem",
)
INDEX_FILES = ("README.md", "cases/INDEX.md", "llms.txt")


def iter_link_files(root: str) -> list[str]:
    paths: list[str] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in {".git", "node_modules"}]
        for name in filenames:
            if name.endswith(".md") or name == "llms.txt":
                paths.append(os.path.join(dirpath, name))
    return paths


def case_basenames(root: str) -> set[str]:
    cases_dir = os.path.join(root, "cases")
    if not os.path.isdir(cases_dir):
        return set()
    return {
        name
        for name in os.listdir(cases_dir)
        if name.endswith(".md") and name != "INDEX.md"
    }


def cases_linked_in(text: str, prefix: str | None) -> set[str]:
    if prefix:
        pat = re.compile(rf"\({re.escape(prefix)}([a-z0-9-]+\.md)(?:#[^)]*)?\)")
    else:
        pat = re.compile(r"(?<![/\w])\(([a-z0-9-]+\.md)(?:#[^)]*)?\)")
    return {match.group(1) for match in pat.finditer(text) if match.group(1) != "INDEX.md"}


def iter_targets(text: str) -> list[str]:
    raws = [match.group(2) for match in LINK.finditer(text)]
    raws.extend(match.group(2) for match in REF_DEF.finditer(text))
    return raws


def scan(root: str) -> list[str]:
    broken: list[str] = []
    files = iter_link_files(root)
    if not files:
        return ["no markdown files found"]

    for path in files:
        text = open(path, encoding="utf-8").read()
        rel = os.path.relpath(path, root)
        for slug in SIBLING_URLS:
            if slug in text:
                broken.append(f"{rel}: sibling-hub '{slug}'")
        if rel == "README.md":
            if re.search(r"^## Related\b", text, flags=re.M):
                broken.append("README.md: ## Related is forbidden (sibling hub)")
            if re.search(r"^## (Purpose|Propósito)\b", text, flags=re.M):
                broken.append("README.md: ## Purpose / Propósito is forbidden")
        for raw_link in iter_targets(text):
            raw = raw_link.split()[0].strip("<>")
            if not raw:
                broken.append(f"{rel} -> (empty link)")
                continue
            if raw.startswith(SKIP_PREFIXES) or raw.startswith("#"):
                continue
            dest = raw.split("#", 1)[0]
            if not dest:
                continue
            target = os.path.normpath(os.path.join(os.path.dirname(path), dest))
            if not os.path.exists(target):
                broken.append(f"{rel} -> {raw}")

    expected = case_basenames(root)
    if not expected:
        broken.append("cases/: no case files found")
        return broken

    maps = {
        "README.md": "cases/",
        "llms.txt": "cases/",
        os.path.join("cases", "INDEX.md"): None,
    }
    for rel, prefix in maps.items():
        path = os.path.join(root, rel)
        if not os.path.exists(path):
            broken.append(f"{rel}: missing index map")
            continue
        text = open(path, encoding="utf-8").read()
        linked = cases_linked_in(text, prefix)
        missing = sorted(expected - linked)
        extra = sorted(linked - expected)
        if missing:
            broken.append(f"{rel}: missing case links {missing}")
        if extra:
            broken.append(f"{rel}: links to unknown cases {extra}")

    for name in INDEX_FILES:
        if not os.path.exists(os.path.join(root, name)):
            broken.append(f"{name}: required index file missing")

    return broken


def main() -> int:
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    broken = scan(root)
    if broken:
        print("Broken relative Markdown links:")
        for item in broken:
            print(f"  {item}")
        return 1
    print("Relative Markdown links: ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
