#!/usr/bin/env python3
"""Flag offensive-security phrasing in skills that run on refusal-prone models.

Security skills here describe defensive work (secure code review, fixes,
regression tests). Attack-oriented wording makes cyber-safety classifiers
(e.g. OpenAI's Daybreak gate in Codex) treat that work as offensive. This
check keeps the wording aligned with what the skill actually does.

Usage: scripts/check_skill_wording.py [SKILL_DIR ...]
Default target: skills/review-app-security. Exit 1 if any term is found.
Suppress a deliberate use with "wording-ok" on the same line.
"""
import pathlib
import re
import sys

TERMS = {
    r"\battack(?:er|ers|s|ing)?\b": "untrusted input / another user / unauthorized caller",
    r"\bexploit\w*": "regression test asserting the safe behavior",
    r"\bmalicious\b": "untrusted / embedded instructions",
    r"\badversarial\b": "untrusted / test fixture",
    r"\bbypass\w*": "skip / not enforced on",
    r"\bpoison\w*": "data integrity / unvalidated data",
    r"\brebinding\b": "re-resolution between validation and connect",
    r"\bSSRF\b": "server-side request destination validation (OWASP API7:2023)",
    r"\bcanary\b": "marker string",
    r"\bleak\w*": "expose / forward",
    r"\btakeover\b": "unauthorized account change",
    r"\bpen(?:etration)?[- ]?test\w*": "(omit; source review only)",
    r"\breproducer\b": "local regression test",
    r"\bpayload\w*": "input / fixture content",
    r"\bweaponi\w*": "(omit)",
    r"\bred[- ]team\w*": "(omit)",
}
PATTERN = re.compile("|".join(f"(?:{t})" for t in TERMS), re.IGNORECASE)


def main(argv):
    root = pathlib.Path(__file__).resolve().parent.parent
    targets = [pathlib.Path(a) for a in argv] or [root / "skills" / "review-app-security"]
    hits = 0
    for target in targets:
        files = [target] if target.is_file() else sorted(
            p for p in target.rglob("*") if p.suffix in {".md", ".yaml", ".yml"})
        for path in files:
            for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                if "wording-ok" in line:
                    continue
                for m in PATTERN.finditer(line):
                    word = m.group(0)
                    hint = next(h for t, h in TERMS.items() if re.fullmatch(t, word, re.IGNORECASE))
                    print(f"{path.relative_to(root) if path.is_relative_to(root) else path}:{n}: '{word}' -> {hint}")
                    hits += 1
    if hits:
        print(f"\n{hits} flagged term(s).", file=sys.stderr)
        return 1
    print("No flagged terms.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
