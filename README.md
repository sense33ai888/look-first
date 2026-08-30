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
  <img src="https://img.shields.io/badge/rules-6-111111?style=flat-square" alt="6 rules">
</p>

---

An agent is handed a template library, a repo, a dataset. It opens one file, forms a
rough idea of what the thing is, and then generates *around* that idea instead of *from*
the thing itself.

The output looks like progress. It quietly misses what was already there.

`look-first` is [andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)
kept whole, extended with the reflex that stops the above — for code, research, documents,
data, diagrams.

## The rules

| | Rule | |
|---|---|---|
| **1** | **Think before building** | State assumptions. Present both readings, don't pick silently. Simpler approach exists → say so. Unclear → name it and ask. |
| **2** | **Inventory, reuse, then build** | Read the resource's entry docs and index *all the way through* — not the first screen. Already exists → use it. |
| **3** | **Simplicity first** | Minimum work that solves the problem. Nothing speculative. 200 lines that could be 50 → rewrite. |
| **4** | **Surgical changes** | Touch only what you must. Every changed line traces to the request. |
| **5** | **Goal-driven execution** | Turn the task into a verifiable goal. Loop until it passes. |
| **6** | **Say what you skipped** | *Did X; skipped Y, add it when Z.* One line, not buried. |

Rules 1, 3, 4 and 5 are karpathy's, kept intact. Rule 2 is the addition and the one that
gets skipped in practice — **rebuilding what already lives here, or a few files over, is
the most common error.** Rule 6 keeps the shortcut visible.

Rule 2 runs **after** you understand the task, never instead of it.
**Read fully, then keep the output small.** The reverse ships a confident wrong answer.

## Before any derivative

Charts, diagrams, summaries, wrappers, "improved" versions:

> ### What does this carry that the thing it derives from doesn't?

No answer → don't build it. Say the existing artifact already covers it.

## What it looks like

**Handed a template library, asked for a chart**

> ❌ Open one file, see roughly how it works, hand-write a generic chart in the underlying
> library. Looks fine — and ignores the 64 purpose-built templates and their entire visual
> language.
>
> ✅ Read `catalog.md`, pick by data shape, open that template's code block, swap the data,
> keep the skeleton.
> → *Used template C8; each row got its own scale because the values span three orders of
> magnitude.*

**Asked to visualise an analysis you already wrote**

> ❌ Build three versions in two libraries.
>
> ✅ *The analysis already states this in a form that reads faster. A diagram here is
> polish, not information — want it anyway?*

**A tool's validator keeps rejecting your input**

> ❌ Reshape the content until the tool accepts it, then ship the reshaped thing.
>
> ✅ *This tool models pipelines; the data is an argument graph. It only passes if I flatten
> it into one chain, which drops the point. Wrong tool — here's what fits.*

**Asked to add a config option**

> ❌ Add the option, a default, a validator, docs for it, and two more options "while we're
> here".
>
> ✅ *Added the one option. Skipped the other two — no caller wants them yet.*

**Told to fix a bug in one caller**

> ❌ Patch the path the ticket names. Ship.
>
> ✅ Grep every caller first. One guard in the shared function is a smaller diff *and* fixes
> the four siblings that were equally broken.

**Something in the request is missing**

> Missing **logistics** (a tool to install, a file to be handed, a login) → say what you
> need and how to provide it, then keep going. Don't stall.
>
> Missing **intent or scope** (the whole task could be wasted work) → stop, name exactly
> what's unclear, ask.

## Never simplify away

Safety-relevant checks · error handling that prevents data loss · anything explicitly
requested · source citations · correctness itself.

These rules govern **how you work**, not how high the bar is.

## Install

**Claude Code**

```bash
/plugin marketplace add sense33ai888/look-first
/plugin install look-first@look-first
```

Or drop `CLAUDE.md` into a project — or into `~/.claude/CLAUDE.md` to make it always-on
everywhere. Or copy `skills/look-first/` into `~/.claude/skills/`.

**OpenClaw**

Copy `.openclaw/skills/look-first/` into your skills directory.

## Files

| Path | What |
|---|---|
| `CLAUDE.md` | Always-on rules. Drop into a project or `~/.claude/`. |
| `skills/look-first/SKILL.md` | Claude Code skill form (on-demand). |
| `.openclaw/skills/look-first/SKILL.md` | OpenClaw skill form. |
| `.claude-plugin/` | Plugin + marketplace manifests. |

Two formats, one skill, no build step, no separate examples file — deliberately. Spreading
the same sixty lines across twenty agent formats would be exactly the unrequested
configurability these rules argue against.

## Working if

Fewer *"that tool already had X"* moments after the fact.
Fewer artifacts that carry no new information.
Clarifying questions landing before the work instead of after the mistake.

## Credits

**Base:** [andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) —
think before coding · simplicity first · surgical changes · goal-driven execution — itself
derived from Andrej Karpathy's observations on LLM coding pitfalls. Its four sections are
kept **in full**; they are rules 1, 3, 4 and 5 here.

**Extended with** [ponytail](https://github.com/DietrichGebert/ponytail) (MIT): the
reuse-first reflex, the guard that comprehension must come *before* shortening, and the
"say what you skipped" output shape.

**Added here:** inventory a resource you were handed before generating from it (rule 2);
the derivative test; the logistics-vs-intent split that decides when to stall and when to
drive; and the generalisation of all of it beyond code.

## License

MIT.
