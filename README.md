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
  <img src="https://img.shields.io/badge/works%20with-Claude%20Code%20%C2%B7%20OpenClaw-111111?style=flat-square" alt="Works with Claude Code and OpenClaw">
  <img src="https://img.shields.io/badge/scope-any%20domain-111111?style=flat-square" alt="Domain agnostic">
</p>

---

An agent is handed a template library, a repo, a dataset. It opens one file, forms a rough
idea of what the thing is, and generates *around* that idea instead of *from* the thing
itself. The output looks like progress and quietly misses what was already there.

`look-first` is [andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)
and [ponytail](https://github.com/DietrichGebert/ponytail) carried verbatim, plus one
section for the miss above, generalised past code to research, documents, data, diagrams.

## Surface is not understanding

The one addition. The rest is the two upstreams, unedited.

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

## The rest

From the upstreams, verbatim — read [`CLAUDE.md`](CLAUDE.md):

| | | from |
|---|---|---|
| **Persistence** | active every response, `full` mode | ponytail |
| **1. Think Before Coding** | state assumptions, surface tradeoffs, ask when unclear | karpathy |
| **2. The Ladder** | stop at the first rung that holds; reuse before you write | ponytail |
| **3. Simplicity First** | minimum that solves it, nothing speculative | both |
| **4. Surgical Changes** | touch only what you must | karpathy |
| **5. Goal-Driven Execution** | verifiable success criteria, one runnable check | both |
| **6. Output** | code first, then ≤3 lines of what you skipped | ponytail |
| **Never simplify away** | trust boundaries, data-loss guards, understanding the problem | ponytail |
| **Boundaries** | governs what you build, not how you talk | ponytail |

## Install

**Claude Code**

```bash
/plugin marketplace add sense33ai888/look-first
/plugin install look-first@look-first
```

Or drop `CLAUDE.md` into a project — or `~/.claude/CLAUDE.md` to make it always-on
everywhere.

**OpenClaw**

```bash
git clone https://github.com/sense33ai888/look-first
cp -r look-first/.openclaw/skills/look-first ~/.openclaw/skills/
```

OpenClaw applies it on tasks and exposes it as `/look-first`. (No ClawHub package
published — the manual copy is the path.)

## Files

| Path | What |
|---|---|
| [`CLAUDE.md`](CLAUDE.md) | The rules. Drop into a project or `~/.claude/`. |
| `skills/look-first/SKILL.md` | Claude Code skill form (same body). |
| `.openclaw/skills/look-first/SKILL.md` | OpenClaw skill form (same body). |
| [`MAINTENANCE.md`](MAINTENANCE.md) | The whole job going forward: track the two upstreams. |
| `.claude-plugin/` | Plugin + marketplace manifests. |

Two formats, one skill, no build step, no separate examples file. Spreading the same rules
across twenty agent formats would be exactly the unrequested configurability they argue
against.

## Credits

**[andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** — think
before coding · simplicity first · surgical changes · goal-driven execution — from Andrej
Karpathy's observations on LLM coding pitfalls. All four sections carried in full.

**[ponytail](https://github.com/DietrichGebert/ponytail)** (MIT) — the lazy senior dev.
Ladder, root-cause rule, simplicity rules, output shape, one-runnable-check, persistence,
boundaries, never-simplify list, "read fully, then be lazy" — all carried in full.

Neither source's text is edited. Dropped: what the two duplicated, the frontmatter and
persona lines, and ponytail's `lite/full/ultra` switcher (kept as one line in Persistence:
`full` mode, fixed). The only renames are `ponytail` → `look-first` in the off-switch and
the ceiling-comment prefix. See [`MAINTENANCE.md`](MAINTENANCE.md).

## License

MIT.
