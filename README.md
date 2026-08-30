# look-first

**Read what you were given before you build something new.**

The most common way an agent wastes a turn: it skims what it was handed, builds a rough
mental model of it, and then generates *around* that model instead of *from* the thing
itself. The output looks like progress and quietly misses what was already there.

Domain-agnostic — code, research, documents, data, diagrams.

## The order

Stop at the first step that resolves the task.

1. **Does this need to exist at all?** Speculative need — skip it, say so in one line.
2. **Does it already exist here?** A prior analysis, an existing file, a template the
   resource ships, a standard tool. → use it. *This is the step that gets skipped.*
3. **Does the given resource already do it?** Read its entry docs and index all the way
   through — not the first screen — and list what it actually provides. Then use it the
   way it was designed to be used.
4. **Only then build**, in the smallest form that carries the information.

The order runs **after** you understand the task, never instead of it.
**Read fully, then keep the output small.** The reverse ships a confident wrong answer.

## Before any derivative

Charts, diagrams, summaries, wrappers, "improved" versions:

> **What does this carry that the thing it derives from doesn't?**

No answer → don't build it.

## What it looks like

**Handed a template library, asked for a chart**

❌ Open one file, see roughly how it works, hand-write a generic chart in the underlying
library. Looks fine; ignores the 64 purpose-built templates and their whole visual
language.

✅ Read `catalog.md`, pick by data shape, open that template's code block, swap the data,
keep the skeleton. → *Used template C8; each row has its own scale because the values
span three orders of magnitude.*

**Asked to visualise an analysis you already wrote**

❌ Build three versions in two libraries.

✅ *The analysis document already states the same content in a form that reads faster.
A diagram here is polish, not information — want it anyway?*

**A tool's validator keeps rejecting your input**

❌ Reshape the content until the tool accepts it, and ship the reshaped thing.

✅ *This tool models pipelines; the data is an argument graph. It only passes if I
flatten it into one chain, which drops the point. Wrong tool — here's what fits.*

## Install

**Claude Code**

```bash
/plugin marketplace add obo-yang/look-first
/plugin install look-first@look-first
```

Or drop `CLAUDE.md` into a project (or `~/.claude/CLAUDE.md` for all projects), or copy
`skills/look-first/` into `~/.claude/skills/`.

**OpenClaw**

Copy `.openclaw/skills/look-first/` into your skills directory.

## Files

| Path | What |
|---|---|
| `CLAUDE.md` | Always-on rules. Drop into a project or `~/.claude/`. |
| `skills/look-first/SKILL.md` | Claude Code skill form (on-demand). |
| `.openclaw/skills/look-first/SKILL.md` | OpenClaw skill form. |
| `.claude-plugin/` | Plugin + marketplace manifests. |

Two formats, one skill, no build step — deliberately. Spreading the same 60 lines across
twenty agent formats would be exactly the unrequested configurability these rules argue
against.

## Working if

Fewer "that tool already had X" moments after the fact. Fewer artifacts that carry no new
information. Clarifying questions land before the work instead of after the mistake.

## Credits

The four-part skeleton follows
[andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) (think
before coding · simplicity · surgical changes · verifiable goals), itself derived from
Andrej Karpathy's observations on LLM coding pitfalls.

The reuse-first reflex and the "understand fully, *then* keep it short" guard come from
[ponytail](https://github.com/DietrichGebert/ponytail) (MIT) — its ladder stops at the
first rung that holds, and it warns that the ladder must run after comprehension, not
instead of it.

`look-first` generalises both beyond code, and adds the step neither has as its centre:
**inventory the resource you were handed before generating from it.** Text is
independently written.

## License

MIT.
