# trylinux_skills

Reusable skills for app development, model research, security reviews, and bar exam prep.

## Skills

| Skill | What it does |
|---|---|
| [`bar-essay-review`](skills/bar-essay-review/SKILL.md) | Grades practice MEE and MPT answers: builds a weighted rubric from an NCBE analysis or point sheet (or drafts one), scores each point, maps to a 1-6 band, and ranks fixes. Written for Sonnet. |
| [`build-accessible-flask-compose-apps`](skills/build-accessible-flask-compose-apps/SKILL.md) | Reproduce the Skeinwise development environment and apply its web/Android design approach, zoom, color-vision palettes, OpenDyslexic, and documented decision rationale. |
| [`research-model-task-fit`](skills/research-model-task-fit/SKILL.md) | Research and benchmark model fit for vision, sourced research, assembly, summaries, and document Q&A with quality, privacy, latency, and actual cost evidence. |
| [`review-app-security`](skills/review-app-security/SKILL.md) | Secure code review of your own web/API/Android/AI app: OWASP Web/API/LLM coverage, untrusted-content handling in AI features, prior-fix verification, and fixes backed by regression tests. Worded for refusal-prone models; see below. |

## Layout

```
skills/
  <skill-name>/
    SKILL.md          # required: frontmatter (name, description) + instructions
    references/       # optional supporting docs
```

## Using a skill

- **Claude.ai:** zip the skill folder (`skills/bar-essay-review`, with `SKILL.md` at the top of the zip's folder) and upload it under Settings > Capabilities > Skills.
- **Claude Code:** copy the skill folder into `~/.claude/skills/` (all projects) or `.claude/skills/` in a project.

## Security skill wording

`review-app-security` is defensive work (review, fix, test), but attack-oriented phrasing makes cyber-safety classifiers on stricter models (e.g. Codex without Daybreak enabled) treat it as offensive. Keep its wording defensive: describe untrusted input rather than attackers, and regression tests that assert the safe behavior rather than exploits or reproducers. Check before committing:

```
python3 scripts/check_skill_wording.py
```

CI runs the same check. Its provenance record lives in `docs/provenance/` so it is not loaded at runtime.

## Disclaimer

Scores are practice estimates, not predictions of bar results. Not affiliated with NCBE. Not legal advice.

## License

MIT. See [LICENSE](LICENSE).
