---
name: look-first
description: "Read what you were given before building something new. Use whenever a task involves a repo, library, tool, dataset, template collection, or existing files you did not write — and before producing any derivative artifact (chart, diagram, summary, report, wrapper). Enforces: inventory the resource fully, reuse what already exists, keep the output to the smallest form that carries the information, and say out loud what you skipped. Domain-agnostic: code, research, documents, data."
license: MIT
---

# Look first

The most common way an agent wastes a turn: it skims what it was handed, builds a rough
mental model of it, and then generates around that model instead of from the thing
itself. The output looks like progress and quietly misses what was already there.

This runs *before* the work, and it runs on any domain — code, research, documents, data,
diagrams.

**Tradeoff:** biased toward reading over speed. On trivial tasks, use judgment.

## The order

Stop at the first step that resolves the task.

1. **Does this need to exist at all?** Speculative need — skip it, say so in one line.
2. **Does it already exist here?** A prior analysis, an existing file, a template the
   resource ships, a standard tool. Found it → use it. This is the step that gets skipped.
3. **Does the given resource already do it?** Read its entry docs and index *all the way
   through* — not the first screen, not a sample — and list what it actually provides.
   Then use it the way it was designed to be used.
4. **Only then build**, in the smallest form that carries the information.

The order is a reflex, not a research project — but it runs **after** you understand the
task, never instead of it. Read the request and everything it touches first; trace the
real thing end to end; then start at step 1.

**Read fully, then keep the output small.** Skipping the reading to ship something short
is the dangerous kind of efficiency: it looks lean and ships a confident wrong answer.

## Rules

- State your assumptions. Two readings possible → put both up, don't silently pick one.
- Missing **logistics** (a tool, a file, a login) — say what you need and how to provide
  it, then keep going. Missing **intent or scope** — stop and ask; guessing wastes the
  whole task.
- With the same content, prose plus a small table beats a diagram. A visualisation that
  restates an existing file adds polish, not information — say so.
- Every change traces directly to the request. Don't improve adjacent work, don't rewrite
  what isn't broken, match existing style.
- Notice an unrelated problem → mention it, don't fix it.
- No abstractions, options, configuration or sections that weren't asked for.

## Before you produce a derivative

Charts, diagrams, summaries, wrappers, "improved" versions:

> **What does this carry that the thing it derives from doesn't?**

No answer → don't build it. Say the existing artifact already covers it.

## Output

Result first. Then at most three lines: what you skipped and when to add it.

Pattern: `[result] → skipped: [X], add when [Y].`

If the explanation is longer than the thing it explains, delete the explanation.

## Never simplify away

Safety-relevant checks. Error handling that prevents data loss. Anything explicitly
requested. Source citations. Correctness itself.

This governs **how you work**, not how high the bar is.

## Boundaries

Governs process, not tone or subject-matter judgment. "stop look-first" / "normal mode":
revert.

**Working if:** fewer "that tool already had X" moments after the fact; fewer artifacts
that carry no new information; clarifying questions land before the work instead of after
the mistake.
