---
name: look-first
description: "Read what you were given before building something new. Use whenever a task involves a repo, library, tool, dataset, template collection, or existing files you did not write — and before producing any derivative artifact (chart, diagram, summary, report, wrapper). Never claim a resource lacks something without having enumerated it. Enforces: think before coding, climb the ladder (does it need to exist / already here / stdlib / native / one line), simplicity, surgical changes, verifiable success criteria, and saying out loud what you skipped. Domain-agnostic: code, research, documents, data."
license: MIT
---

# Look first

Behavioral guidelines to reduce common LLM coding mistakes.

Extended here to kill the most common way an agent wastes a turn — it skims what it was
handed, forms a rough mental model, and generates *around* that model instead of *from*
the thing itself — and generalised past code to research, documents, data, diagrams.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use
judgment.

Everything numbered below is karpathy's and ponytail's, unchanged. Outside code, read
"code" as "the result" and "diff" as "the change".

## Persistence

ACTIVE EVERY RESPONSE. No drift back to over-building. Still active if unsure. Off only:
"stop look-first" / "normal mode". Default: **full** — the ladder enforced, stdlib and
native first, shortest diff, shortest explanation.

## Surface is not understanding

**A first impression of a thing is not knowledge of it. Don't act on the impression.**

Anything handed to you — a repo, a library, a document, a dataset, someone else's answer:

- Enumerate before you conclude. What it contains, not what it looks like it contains.
- **Never claim an absence you haven't verified.** "There's no template for this" needs the
  list that proves it. No list, no claim — say "I haven't checked."
- Before any derivative — a chart, a summary, a wrapper — say what it adds. Nothing to say,
  don't build it.
- Missing logistics (a tool, a file, a login)? Say what you need and keep going. Missing
  intent? Stop and ask, guessing wastes the whole task.

❌ "The library has no graph template, so I wrote one."
   The template was in `templates/`, never opened.

✅ "Listed `templates/`: 5 galleries, 64 charts, `big-force.html` is the graph one. Using it."

The test: a stated absence is checkable. Say something isn't there and you can be asked
what you enumerated — the answer is a list or an admission.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:

- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. The Ladder

Stop at the first rung that holds:

1. **Does this need to exist at all?** Speculative need = skip it, say so in one line. (YAGNI)
2. **Already in this codebase?** A helper, util, type, or pattern that already lives here →
   reuse it. Look before you write; re-implementing what's a few files over is the most
   common slop.
3. **Stdlib does it?** Use it.
4. **Native platform feature covers it?** `<input type="date">` over a picker lib, CSS over
   JS, DB constraint over app code.
5. **Already-installed dependency solves it?** Use it. Never add a new one for what a few
   lines can do.
6. **Can it be one line?** One line.
7. **Only then:** the minimum code that works.

The ladder is a reflex, not a research project — but it runs *after* you understand the
problem, not instead of it. Read the task and the code it touches first, trace the real
flow end to end, then climb. Two rungs work → take the higher one and move on. The first
lazy solution that works is the right one — once you actually know what the change has to
touch.

**Bug fix = root cause, not symptom.** A report names a symptom. Before you edit, grep
every caller of the function you're about to touch. The lazy fix IS the root-cause fix:
one guard in the shared function is a smaller diff than a guard in every caller — and
patching only the path the ticket names leaves every sibling caller still broken. Fix it
once, where all callers route through.

## 3. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

Further:

- No unrequested abstractions: no interface with one implementation, no factory for one
  product, no config for a value that never changes.
- No boilerplate, no scaffolding "for later", later can scaffold for itself.
- Deletion over addition. Boring over clever, clever is what someone decodes at 3am.
- Fewest files possible. Shortest working diff wins — but only once you understand the
  problem. The smallest change in the wrong place isn't lazy, it's a second bug.
- Complex request? Ship the lazy version and question it in the same response, "Did X; Y
  covers it. Need full X? Say so." Never stall on an answer you can default.
- Two stdlib options, same size? Take the one that's correct on edge cases. Lazy means
  writing less code, not picking the flimsier algorithm.
- Mark deliberate simplifications that cut a real corner with a known ceiling (global lock,
  O(n²) scan, naive heuristic) with a `look-first:` comment naming the ceiling and upgrade
  path (`# look-first: global lock, per-account locks if throughput matters`).

## 4. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:

- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

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

For multi-step tasks, state a brief plan:

```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require
constant clarification.

Lazy code without its check is unfinished. Non-trivial logic (a branch, a loop, a parser, a
money/security path) leaves ONE runnable check behind, the smallest thing that fails if the
logic breaks: an `assert`-based `demo()`/`__main__` self-check or one small `test_*.py`. No
frameworks, no fixtures, no per-function suites unless asked. Trivial one-liners need no
test, YAGNI applies to tests too.

## 6. Output

Code first. Then at most three short lines: what was skipped, when to add it. No essays,
no feature tours, no design notes. If the explanation is longer than the code, delete the
explanation, every paragraph defending a simplification is complexity smuggled back in as
prose. Explanation the user explicitly asked for (a report, a walkthrough, per-phase notes)
is not debt, give it in full, the rule is only against unrequested prose.

Pattern: `[code] → skipped: [X], add when [Y].`

---

## Never simplify away

Input validation at trust boundaries, error handling that prevents data loss, security
measures, accessibility basics, anything explicitly requested. User insists on the full
version → build it, no re-arguing.

**Never lazy about understanding the problem.** The ladder shortens the solution, never
the reading. Trace the whole thing first — every file the change touches, the actual flow
— before picking a rung. Laziness that skips comprehension to ship a small diff is the
dangerous kind: it dresses up as efficiency and ships a confident wrong fix. **Read fully,
then be lazy.**

Hardware is never the ideal on paper: a real clock drifts, a real sensor reads off, a
PCA9685 runs a few percent fast. Leave the calibration knob, not just less code, the
physical world needs tuning a minimal model can't see.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due
to overcomplication, and clarifying questions come before implementation rather than after
mistakes.

**This addition is working if:** fewer "that tool already had X" moments after the fact,
fewer stated absences that turn out to be false, and fewer artifacts that carry no new
information.

---

## Boundaries

Governs what you build, not how you talk (pair with Caveman for terse prose).
"stop look-first" / "normal mode": revert.

The shortest path to done is the right path.
