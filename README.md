# trylinux_skills

Reusable skills for app development, model research, and bar exam prep.

## Skills

| Skill | What it does |
|---|---|
| [`bar-essay-review`](skills/bar-essay-review/SKILL.md) | Grades practice MEE and MPT answers: builds a weighted rubric from an NCBE analysis or point sheet (or drafts one), scores each point, maps to a 1-6 band, and ranks fixes. Written for Sonnet. |
| [`build-accessible-flask-compose-apps`](skills/build-accessible-flask-compose-apps/SKILL.md) | Reproduce the Skeinwise development environment and apply its web/Android design approach, zoom, color-vision palettes, OpenDyslexic, and documented decision rationale. |
| [`research-model-task-fit`](skills/research-model-task-fit/SKILL.md) | Research and benchmark model fit for vision, sourced research, assembly, summaries, and document Q&A with quality, privacy, latency, and actual cost evidence. |

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

## Disclaimer

Scores are practice estimates, not predictions of bar results. Not affiliated with NCBE. Not legal advice.

## License

MIT. See [LICENSE](LICENSE).
