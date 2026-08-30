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
and [ponytail](https://github.com/DietrichGebert/ponytail) kept whole, deduplicated, and
extended past code — to research, documents, data, diagrams.

## Surface is not understanding

The addition. Everything numbered below is karpathy's and ponytail's, unchanged.

> A first impression of what you were given is not knowledge of it — a repo, a library, a
> document, a dataset, someone else's answer. Do not act on the impression.
>
> - **Enumerate before you conclude.** What it actually contains, not what it looks like it contains.
> - **Never claim absence you haven't verified.** *"There's no X here"* requires the list. Otherwise say *"I haven't checked."*
> - **Before any derivative, ask what it adds.** No answer → don't build it.
> - **Missing logistics → drive. Missing intent → stop and ask.**

The second bullet is the one with teeth: a stated absence is checkable. Ask *"what did you
enumerate?"* and the answer is either a list or an admission.

## The rules

| | Rule | | From |
|---|---|---|---|
| **1** | **Think before coding** | State assumptions. Present both readings, don't pick silently. Simpler approach exists → say so. Unclear → name it and ask. | karpathy |
| **2** | **The ladder** | Stop at the first rung that holds: needs to exist? · already in this codebase? · stdlib? · native? · installed dep? · one line? · then minimum. | ponytail |
| **3** | **Simplicity first** | Minimum code that solves the problem. Nothing speculative. 200 lines that could be 50 → rewrite. | both |
| **4** | **Surgical changes** | Touch only what you must. Every changed line traces to the request. | karpathy |
| **5** | **Goal-driven execution** | Turn the task into a verifiable goal. Loop until it passes. Leave one runnable check. | both |
| **6** | **Output** | Code first, then ≤3 lines: *did X; skipped Y, add when Z.* | ponytail |

Plus **Persistence**, **Never simplify away** and **Boundaries**, from ponytail.

The ladder runs **after** you understand the problem, never instead of it.
**Read fully, then be lazy.** The reverse ships a confident wrong answer.

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
derived from Andrej Karpathy's observations on LLM coding pitfalls. All four sections kept
**in full**: rules 1, 3, 4, 5.

**Merged with** [ponytail](https://github.com/DietrichGebert/ponytail) (MIT) — the lazy
senior dev. Its ladder, root-cause rule, simplicity rules, output shape, one-runnable-check
rule, persistence, boundaries, never-simplify list and "read fully, then be lazy" kept
**in full**. Dropped only what the two sources duplicated, plus the `lite/full/ultra`
switcher — this is **full** mode, fixed.

Neither source's text is edited. Their sections are verbatim; the only renames are
`ponytail` → `look-first` in the mode-off phrase and the ceiling-comment prefix.

**Added here — the "Surface is not understanding" section, and nothing else:** enumerate
before concluding, never claim an absence you haven't verified, the derivative test, and
the logistics-vs-intent split that decides when to stall and when to drive. Plus the
generalisation of all of it past code.

## License

MIT.
