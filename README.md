<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo-dark.svg">
    <img src="assets/logo.svg" width="150" alt="look-first">
  </picture>
</p>

<h1 align="center">look-first</h1>

<p align="center">
  <em>Read what you were given before you build something new.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-111111?style=flat-square" alt="MIT license">
  <img src="https://img.shields.io/badge/works%20with-Claude%20Code%20%C2%B7%20Codex%20%C2%B7%20OpenClaw-111111?style=flat-square" alt="Works with Claude Code, Codex, and OpenClaw">
  <img src="https://img.shields.io/badge/scope-any%20domain-111111?style=flat-square" alt="Domain agnostic">
</p>

---

An agent is handed a template library, a repo, a dataset. It opens one file, forms a rough
idea of what the thing is, and generates *around* that idea instead of *from* the thing
itself. The output looks like progress and quietly misses what was already there.

`look-first` is [andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)
and [ponytail](https://github.com/DietrichGebert/ponytail) carried verbatim, plus one
section for the miss above, generalised past code to research, documents, data, diagrams.
Project Git checkpoints and handoff notes now let different tools continue the same work.

## Surface is not understanding

The original addition. The inherited behavioral rules remain unchanged.

> **A first impression of a thing is not knowledge of it. Don't act on the impression.**
>
> Anything handed to you — a repo, a library, a document, a dataset, someone else's answer:
>
> - Enumerate before you conclude. What it contains, not what it looks like it contains.
> - **Never claim an absence you haven't verified.** "There's no template for this" needs
>   the list that proves it. No list, no claim — say "I haven't checked."
> - Before any derivative — a chart, a summary, a wrapper — say what it adds. Nothing to
>   say, don't build it.
> - Missing logistics (a tool, a file, a login)? Say what you need and keep going. Missing
>   intent? Stop and ask, guessing wastes the whole task.

**Failure it is named after:**

> ❌ "The library has no graph template, so I wrote one." — the template was in
> `templates/`, never opened.
>
> ✅ "Listed `templates/`: 5 galleries, 64 charts, `big-force.html` is the graph one.
> Using it."

The test: a stated absence is checkable. Say something isn't there and you can be asked
what you enumerated — the answer is a list or an admission.

## Shared rules, project history, and handoff

Use one project folder as the shared workspace. The original look-first rules live in
[`AGENTS.md`](AGENTS.md), followed by the **Project history and handoff** section.
[`CLAUDE.md`](CLAUDE.md) imports that file. The packaged skills carry the same body so
they also work when installed independently.

The minimum for continuity is **look-first + a brief project description + a current
`STATUS.md`**. Keep the description in your existing README or project instructions:
what the project is for, its boundaries, key files, and relevant run/check commands.
Reuse existing handoff notes if they already serve this purpose. No extra `records/`,
`memory/`, or `runbooks/` directories are required; add them only when the project needs them.

A typical project has:

```text
my-project/
├── .git/          Created and managed by Git, not copied from this template
├── .gitignore     Project-specific exclusions
├── AGENTS.md      Shared look-first rules and project conventions
├── CLAUDE.md      @AGENTS.md
├── README.md      Project purpose and how to use or verify it
├── STATUS.md      Current objective, progress, checks, and next step
└── ...            The actual project files
```

Git records saved file versions; it does not automatically save every edit or transfer
chat history. A commit is a checkpoint, not proof that the work is complete or verified.
`STATUS.md` supplies the short handoff context that file history alone cannot provide.
Keep it current at milestones or handoffs, not after every reply. Check its claims
against the actual files and Git state before continuing. Save at meaningful milestones
so an unexpected interruption does not leave the only useful context in chat. A fresh
session should be able to identify the goal, verification gaps, and next concrete action
from the project files.

### Set up a project

For a **new project with no existing instruction files**, copy these files from a local
checkout of look-first:

| Source | Destination in your project |
|---|---|
| `AGENTS.md` | `AGENTS.md` |
| `CLAUDE.md` | `CLAUDE.md` |
| `templates/STATUS.md` | `STATUS.md`, filled in for this project |
| `templates/gitignore` | `.gitignore`, adapted to this project |

Keep the project's own README and add its real run/check commands and constraints.
For an existing project, merge these rules into its established instructions and ignore
patterns; do not overwrite them. Never replace existing handoff notes with a blank
template. If CLAUDE.md already imports AGENTS.md, add the common rules only once.

Check whether the folder is already inside a Git repository before initializing.
Reuse the repository that owns the project, including a parent repository or worktree.
For a standalone new repository, review the files and exclusions, then commit the
starting state before substantive edits. Do not copy this repository's `.git`,
remote settings, or completed `STATUS.md` into another project. A linked worktree may
have a `.git` **file** instead of a directory; use Git to inspect and manage it.

### Connect your tools

| Tool | Entry point |
|---|---|
| Codex | Reads the project's `AGENTS.md` through its instruction discovery. |
| Claude Code | Reads `CLAUDE.md`; its `@AGENTS.md` line imports the shared rules. |
| OpenClaw | Ensure its active workspace instructions tell it to read the target project's `AGENTS.md`, relevant README, and `STATUS.md` before editing. |

For OpenClaw, a tool working directory can differ from the managed agent workspace where
bootstrap instructions and memory are loaded. Pointing tools at a repository is not by
itself proof that its AGENTS.md was loaded. Preserve the existing workspace instructions,
and make the project-reading step explicit. Each tool still needs access to the project
and permission to perform the requested operations.

These are local-file workflows for tools such as Claude Code, not a claim that an ordinary
web chat can automatically access a local folder. For another machine, clone or synchronize
the repository through an authorized remote.

Official references:
[Codex instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md),
[Claude Code imports](https://code.claude.com/docs/en/memory#import-additional-files),
[OpenClaw workspace and working directory](https://docs.openclaw.ai/gateway/config-agents/workspace-and-bootstrap).

### Work and switch tools

1. Read the instructions and current handoff; inspect Git status and relevant history.
2. Make the requested change while preserving unrelated work.
3. Run the relevant verification, update the handoff if needed, and commit only the
   task's changes with a useful message.
4. At a switch, report what is complete, what is unverified, and what to do next.
   Label unfinished checkpoints as WIP instead of claiming completion.

Questions and read-only reviews do not require initialization, status updates, or commits.
The normal checkpoint is a coherent milestone, not every reply. If Git is unavailable,
identity is missing, or permissions block a commit, record the handoff and report the
limitation rather than pretending the checkpoint exists.

Use **one writer per working tree** when tools take turns. For simultaneous edits,
give each writer a separate branch and worktree, then review and integrate the results.
Read-only inspection can share the working tree.
[Git worktrees](https://git-scm.com/docs/git-worktree)

Local Git history is not an off-machine backup. For recovery from a lost folder or disk,
configure an appropriate remote, usually a private repository, and push completed
checkpoints within the user's authorization. Standing authorization can cover later
pushes; do not ask repeatedly when it already applies. Untracked or ignored source
material needs its own backup if it must be recoverable.
[Git remotes](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)

### Confirm the setup

Start a fresh session and confirm which instruction files were loaded. In Claude Code,
use `/context` and `/memory`; for Codex, inspect its instruction-loading logs when needed.
Then check observable behavior: it inspected the relevant files, preserved unrelated
changes, recorded verification honestly, and created the stated checkpoint.

A repeated greeting or name does not prove that instructions were loaded or followed.
[Claude Code configuration checks](https://code.claude.com/docs/en/debug-your-config)

## Install as a skill

The project-file setup above provides the shared startup rules. The existing skill
installation routes remain available.

**Claude Code**

```bash
/plugin marketplace add sense33ai888/look-first
/plugin install look-first@look-first
```

**OpenClaw**

```bash
git clone https://github.com/sense33ai888/look-first
cp -r look-first/.openclaw/skills/look-first ~/.openclaw/skills/
```

Preserve any local customization when updating an existing installation. The packaged
skills are self-contained; they do not depend on AGENTS.md being next to the installed
skill. No ClawHub package is published here.

## Files and maintenance

| Path | Purpose |
|---|---|
| [`AGENTS.md`](AGENTS.md) | Canonical rules, with the original body preserved and the project workflow appended. |
| [`CLAUDE.md`](CLAUDE.md) | Claude Code import of AGENTS.md. |
| `skills/look-first/SKILL.md` | Claude Code skill package. |
| `.openclaw/skills/look-first/SKILL.md` | OpenClaw skill package. |
| [`templates/STATUS.md`](templates/STATUS.md) | Handoff starter for a new project. |
| [`templates/gitignore`](templates/gitignore) | Minimal ignore starter; review and extend for each project. |
| [`STATUS.md`](STATUS.md) | This repository's own current handoff, not a project template. |
| [`scripts/sync_skills.py`](scripts/sync_skills.py) | Synchronize the entrypoint and packaged rule bodies. |
| [`MAINTENANCE.md`](MAINTENANCE.md) | Upstream fidelity, local additions, and synchronization checks. |
| `.claude-plugin/` | Claude Code plugin and marketplace manifests. |

Edit AGENTS.md, then run:

```bash
python3 scripts/sync_skills.py
python3 scripts/sync_skills.py --check
```

There is no runtime build step. Keep the generated skills checked in so installation
works directly from the repository.

## Credits

**[andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** —
think before coding, simplicity first, surgical changes, and goal-driven execution.

**[ponytail](https://github.com/DietrichGebert/ponytail)** (MIT) —
the ladder, root-cause rule, simplicity rules, output shape, runnable check, persistence,
boundaries, and never-simplify guidance.

The inherited behavioral rules are preserved from the previous look-first version.
The original **Surface is not understanding** section remains intact. **Project history
and handoff** is a separate local addition. See MAINTENANCE.md for the inherited deliberate
drops and the procedure for future upstream updates.

## License

MIT.
