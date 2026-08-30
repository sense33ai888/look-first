---
name: look-first
description: "Read what you were given before building something new. Use whenever a task involves a repo, library, tool, dataset, template collection, or existing files you did not write — and before producing any derivative artifact (chart, diagram, summary, report, wrapper). Enforces: think before building, inventory the resource fully, reuse what already exists, keep it simple, make surgical changes, define verifiable success criteria, and say out loud what you skipped. Domain-agnostic: code, research, documents, data."
license: MIT
---

# Look first

Behavioural guidelines that reduce common LLM mistakes, and kill the most common way an
agent wastes a turn: it skims what it was handed, forms a rough mental model, and then
generates *around* that model instead of *from* the thing itself. The output looks like
progress and quietly misses what was already there.

Domain-agnostic — code, research, documents, data, diagrams.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use
judgment.

## 1. Think Before Building

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:

- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them — don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

The cost of guessing decides whether "stop and ask" or "keep going" is right:

- **Missing logistics** (a tool to install, a file to be handed, a login) — say plainly
  what you need and how to provide it, then continue. Don't stall on it.
- **Missing intent or scope** (the whole task could be wasted work) — stop, name exactly
  what is unclear, ask.

## 2. Inventory, Reuse, Then Build

**Read what you were given before you build something new.**

Before producing anything *from* something you were handed — a repo, a library, a tool, a
dataset, an existing file:

- **Read its entry documents and index all the way through.** Not the first screen, not a
  sample. List what it actually provides.
- Check whether the thing you are about to make already exists: a template it ships, a
  prior analysis, an existing file, a standard tool. If it does, use it.
- Use it the way it was designed to be used, or say why you're not.

**Rebuilding what already lives here — or a few files over — is the most common error.**

Read fully, *then* keep the output small. The reverse — skipping the reading to ship
something short — is how you ship a confident wrong answer.

## 3. Simplicity First

**Minimum work that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

Applies past code. With the same content, prose plus a small table beats a diagram. Before
building any derivative — a chart, a summary, a wrapper, an "improved" version — answer:

> **What does this carry that the thing it derives from doesn't?**

No answer → don't build it. Say the existing artifact already covers it.

## 4. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing work:

- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it — don't delete it.

When your changes create orphans:

- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 5. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:

- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"
- "Summarise the record" → "No line contradicts the source; every figure traces to a file"

For multi-step tasks, state a brief plan:

```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require
constant clarification.

## 6. Say What You Skipped

Deviating from how a resource is meant to be used, or cutting a real corner: one line, out
loud, not buried.

Pattern: *did X; skipped Y, add it when Z.*

If the explanation is longer than the thing it explains, delete the explanation.

## Never simplify away

Safety-relevant checks. Error handling that prevents data loss. Anything explicitly
requested. Source citations. Correctness itself.

These guidelines govern **how you work**, not how high the bar is.

## Boundaries

Governs process, not tone or subject-matter judgment. "stop look-first" / "normal mode":
revert.

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due
to overcomplication, clarifying questions come before implementation rather than after
mistakes, fewer "that tool already had X" moments after the fact, and fewer artifacts that
carry no new information.
