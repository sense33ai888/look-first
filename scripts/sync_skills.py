#!/usr/bin/env python3
"""Keep packaged skills and the Claude entrypoint aligned with AGENTS.md."""

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report drift without writing")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    marker = "\n## Persistence\n"
    canonical = (root / "AGENTS.md").read_text(encoding="utf-8")
    _, found, body = canonical.partition(marker)
    if not found:
        parser.error("AGENTS.md has no Persistence section")

    expected = {root / "CLAUDE.md": "@AGENTS.md\n"}
    for relative in ("skills/look-first/SKILL.md", ".openclaw/skills/look-first/SKILL.md"):
        path = root / relative
        prefix, found, _ = path.read_text(encoding="utf-8").partition(marker)
        if not found:
            parser.error(f"{relative} has no Persistence section; restore its package header")
        expected[path] = prefix + marker + body

    changed = [path for path, text in expected.items()
               if path.read_text(encoding="utf-8") != text]
    if args.check:
        for path in changed:
            print(f"Out of sync: {path.relative_to(root)}")
        if not changed:
            print("CLAUDE.md and both packaged skills match AGENTS.md.")
        return bool(changed)

    for path in changed:
        path.write_text(expected[path], encoding="utf-8")
        print(f"Updated {path.relative_to(root)}")
    if not changed:
        print("Already in sync.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
