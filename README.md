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
  <img src="https://img.shields.io/badge/size-60%20lines-111111?style=flat-square" alt="60 lines">
</p>

---

An agent is handed a template library, a repo, a dataset. It opens one file, forms a
rough idea of what the thing is, and then generates *around* that idea instead of *from*
the thing itself.

The output looks like progress. It quietly misses what was already there.

`look-first` is the reflex that stops it — for code, research, documents, data, diagrams.

## The order

Stop at the first step that resolves the task.

| | Step | |
|---|---|---|
| **1** | **Does this need to exist at all?** | Speculative need — skip it, say so in one line. |
| **2** | **Does it already exist here?** | A prior analysis, an existing file, a template the resource ships, a standard tool. → use it. |
| **3** | **Does the given resource already do it?** | Read its entry docs and index *all the way through* — not the first screen. List what it actually provides. Then use it the way it was designed to be used. |
| **4** | **Only then build** | In the smallest form that carries the information. |

Step 2 is the one that gets skipped. Rebuilding what already lives here — or a few files
over — is the most common error.

The order runs **after** you understand the task, never instead of it.
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
/plugin marketplace add obo-yang/look-first
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

The four-part skeleton follows
[andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) — think
before coding · simplicity first · surgical changes · verifiable goals — itself derived
from Andrej Karpathy's observations on LLM coding pitfalls.

The reuse-first reflex, and the guard that comprehension must come *before* shortening,
come from [ponytail](https://github.com/DietrichGebert/ponytail) (MIT): its ladder stops
at the first rung that holds, and it warns that the ladder runs after you understand the
problem, never instead of it.

`look-first` generalises both beyond code and adds the step neither has at its centre:
**inventory the resource you were handed before you generate from it.** Text is
independently written.

## License

MIT.
