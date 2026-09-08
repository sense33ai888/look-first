# Maintenance

**look-first tracks two upstreams and maintains its own project workflow. Keep their scopes explicit.**

The numbered sections, Persistence, Never simplify away and Boundaries are verbatim from:

- [`multica-ai/andrej-karpathy-skills`](https://github.com/multica-ai/andrej-karpathy-skills) → `CLAUDE.md`
- [`DietrichGebert/ponytail`](https://github.com/DietrichGebert/ponytail) → `.openclaw/skills/ponytail/SKILL.md`

The local sections are **Surface is not understanding** and **Project history and handoff**.
The latter was appended without rewriting the inherited behavioral rules.
Project entrypoints, handoff templates, and synchronization tooling are also maintained here.

## When an upstream changes

1. Diff its file against what we carry.
2. New or reworded rules → copy them in verbatim. Match their placement.
3. If they add a switcher, telemetry, a persona, or per-agent format sprawl → **skip it**,
   note why in the commit. look-first keeps `full` mode and checked-in entrypoints;
   no runtime build is required.
4. If a change contradicts *Surface is not understanding* → keep both, and say so in the
   commit. This original addition does not get overwritten, but it also does not
   silently diverge.
5. Re-run the fidelity check (below). Update `README.md` credits if section names moved.
6. One commit per upstream. Message names the upstream commit you synced to.
7. Keep **Project history and handoff** separate from upstream imports. Review a proposed
   update for compatibility with that workflow before integrating it. Do not silently
   overwrite the local workflow or change the inherited rules as part of a packaging edit.

## When you touch Surface is not understanding

Same voice as the upstreams, always:

- Bold thesis line under the heading.
- One lead-in sentence, then terse imperative bullets.
- A concrete ❌ / ✅ pair — a real failure, not a hypothetical.
- A `The test:` closer.

New rules only from a real miss that the current text did not catch. No speculative rules.

## Fidelity check

Every content line of each upstream is either present verbatim or listed here as a
deliberate drop.

**Deliberate drops (do not re-add):**

- Frontmatter, persona lines ("lazy senior developer", "paged at 3am"), homepage/description.
- ponytail's `## Intensity` table and the `lite/full/ultra` switcher + its cache example.
  Kept as prose in `## Persistence`: *Default: full — the ladder enforced…*
- karpathy's standalone intro line and its "working if" phrasing — replaced by our intro
  and our own "working if", which sit outside the numbered sections.
- Cross-references to sibling skills (Caveman).

Renames applied throughout: `ponytail` → `look-first` in the off-switch phrase and the
`look-first:` ceiling-comment prefix.

Script:

```
python3 - <<'PY'
import pathlib, re
def key(s): return re.sub(r'[^a-z0-9]','',s.lower())
K = key(pathlib.Path('AGENTS.md').read_text())
def lines(t):
    out=[]
    for l in t.split('\n'):
        l=re.sub(r'^\d+\.\s*','',l.strip().lstrip('-').strip())
        if len(key(l))>25 and not l.startswith('#'): out.append(l)
    return out
for name,path in (('karpathy','../andrej-karpathy-skills/CLAUDE.md'),
                  ('ponytail','../ponytail/.openclaw/skills/ponytail/SKILL.md')):
    src=pathlib.Path(path).read_text()
    miss=[l for l in lines(src) if key(l) not in K]
    print(f'{name}: {len(miss)} lines not verbatim — each must be a deliberate drop above')
    for m in miss: print('  ', m[:100])
PY
```

Clone both upstreams next to this repo, run it, reconcile every reported line against the
deliberate-drops list.

## Canonical rules and generated entrypoints

Edit `AGENTS.md`. It contains the original look-first text followed by the local
**Project history and handoff** section. Do not rewrite the inherited numbered sections
when updating this project workflow.

`AGENTS.md`, `skills/look-first/SKILL.md`, and
`.openclaw/skills/look-first/SKILL.md` share the exact body from `## Persistence`
to the end. The skills keep their existing package headers and introductions so they
remain independently installable. `CLAUDE.md` contains only `@AGENTS.md`.

```bash
python3 scripts/sync_skills.py
python3 scripts/sync_skills.py --check
```

The check fails on an out-of-sync body or Claude entrypoint and does not modify files.
Run it before committing. Keep the generated files in Git; consumers do not need Python
or a generation step to install the skill.

## Project workflow and templates

Keep the Git and handoff instructions scoped to authorized file-changing project tasks.
Preserve pre-existing work, distinguish verified milestones from WIP checkpoints, and
respect the user's remote-push authorization. Do not add ceremonial output requirements
as a proxy for verifying instruction loading or compliance.

`templates/STATUS.md` is the blank handoff starter. `STATUS.md` describes this repository's
actual state. Do not copy the latter into another project. `templates/gitignore` is a
starter that must be adapted; it is not a promise to catch every secret or disposable file.

Update README setup instructions when entrypoints change. Bump the plugin version for
shipped behavior or packaging changes, preserving the marketplace's existing manifest
shape. Check the import target, relative documentation links, JSON manifests, and
independent skill bodies after updates. Do not create a remote repository or push merely
because a template describes those options; the current task must authorize the action.
