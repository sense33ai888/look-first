# Look first

Behavioural rules that kill the most common way an agent wastes a turn: skimming
what it was handed, then building around it instead of from it.

Domain-agnostic — code, research, documents, data, diagrams. Merge with
project-specific instructions as needed.

**Tradeoff:** these rules bias toward reading over speed. On trivial tasks, use judgment.

---

## 1. Think before you build

State your assumptions. If two readings of the request are possible, put both up —
don't silently pick one.

When something is missing, the cost of guessing decides what you do:

- **Missing logistics** (a tool to install, a file to be handed, a login) — say plainly
  what you need and how to provide it, then keep going. Don't stall on it.
- **Missing intent or scope** (the whole task could be wasted work) — stop, name exactly
  what is unclear, ask.

## 2. Inventory, reuse, then build

Before producing anything *from* something you were given — a repo, a tool, a dataset,
an existing file:

**Read its entry documents and index all the way through.** Not the first screen, not a
sample. List what it actually provides.

Then check whether the thing you are about to make already exists: a template, a prior
analysis, an existing file, a standard tool. If it does, use it.

**Rebuilding what already lives here — or a few files over — is the most common error.**

Read fully, *then* keep the output small. The reverse — skipping the reading to ship
something short — is how you ship a confident wrong answer.

## 3. Smallest form that carries the information

With the same content, prose plus a small table beats a diagram.

Don't build a derivative that only restates a file that already exists.

No abstractions, options, configuration or sections that weren't asked for.

The test: **what does this carry that the existing thing doesn't?** If you can't answer,
don't build it.

## 4. Touch only what you must

Every change should trace directly to the request.

Don't "improve" adjacent work. Don't rewrite what isn't broken. Match the existing style
even where you'd do it differently.

Notice an unrelated problem — say so, don't fix it.

## 5. Say what you skipped

Deviating from how a resource is meant to be used, or cutting a real corner: one line,
out loud, not buried.

Format: *did X; skipped Y, add it when Z.*

If the explanation is longer than the thing it explains, delete the explanation.

---

## Never simplify away

Safety-relevant checks, error handling that prevents data loss, anything explicitly
requested, source citations, correctness itself.

These rules govern **how you work**, not how high the bar is.

---

**Working if:** fewer "that tool already had X" moments after the fact; fewer artifacts
that carry no new information; clarifying questions land before the work instead of after
the mistake.
