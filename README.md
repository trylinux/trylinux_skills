# trylinux_skills

Claude skills, starting with bar exam prep.

## Skills

| Skill | What it does |
|---|---|
| [`bar-essay-review`](skills/bar-essay-review/SKILL.md) | Reviews practice MEE and MPT answers using NCBE's relative 1-6 grading model, issue-based checklists, and writing-quality checks. |

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
