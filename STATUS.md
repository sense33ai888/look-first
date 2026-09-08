# Current status

## Current objective
Provide one shared look-first rule source for Claude Code, Codex, and OpenClaw,
with Git checkpoints and concise project handoffs.

## Completed
- Preserved the original look-first behavioral text in AGENTS.md.
- Added project-scoped Git and handoff instructions; CLAUDE.md imports AGENTS.md.
- Synchronized both independently installable skills and updated the plugin to 1.1.0.
- Added a handoff template, ignore starter, and synchronization/check command.
- Clarified the minimum continuity setup in 1.1.1: existing project description plus
  current handoff, concrete next steps, and milestone saves before unexpected interruptions.
  Extra directories and duplicate notes are not required.
- Documented setup, OpenClaw workspace routing, concurrent worktrees, and authorized remotes.
- Explained the import direction, the reversed-pointer failure, and the distinction
  between code-formatted documentation examples and bare imports in actual CLAUDE.md files.

## Remaining
- Confirm loading and handoff behavior in the user's actual Claude Code, Codex,
  and OpenClaw installations; those application sessions were not exercised here.
- Observe real usage before changing the inherited behavioral rules.

## Verification
- `python3 scripts/sync_skills.py --check` passes.
- The Claude Code skill passes the skill-creator frontmatter/body validator.
- The OpenClaw skill keeps its supported `homepage` field; the Codex-specific validator
  rejects that OpenClaw-only key, so its shared body and YAML structure were checked separately.
- Both plugin JSON manifests parse successfully.
- The original CLAUDE.md text is preserved verbatim at the start of AGENTS.md.
- For 1.1.1, checked that all text before Project history and handoff is unchanged
  from the preceding commit; checked package synchronization, JSON, and whitespace.
- Markdown local links and whitespace checks pass.
- Checked README import examples retain literal @ characters and code formatting;
  confirmed CLAUDE.md remains exactly the bare import line. Runtime loading remains untested.

## Next step
Try the documented project-file setup in one project and confirm that a fresh session
can identify the instructions, current objective, verification gaps, and next action.

## Important decisions
- AGENTS.md is the canonical source; generated skills stay checked in for direct installation.
- The upstream behavioral rules remain intact. Git and handoff are a separate local addition.
- STATUS.md is a concise handoff, not a transcript or duplicate commit log.
- This file describes look-first itself. Use templates/STATUS.md for another project.
