# Maintenance

**look-first tracks two upstreams. Maintenance is keeping up with them, and nothing else.**

The numbered sections, Persistence, Never simplify away and Boundaries are verbatim from:

- [`multica-ai/andrej-karpathy-skills`](https://github.com/multica-ai/andrej-karpathy-skills) → `CLAUDE.md`
- [`DietrichGebert/ponytail`](https://github.com/DietrichGebert/ponytail) → `.openclaw/skills/ponytail/SKILL.md`

Only one section is ours: **Surface is not understanding**.

## When an upstream changes

1. Diff its file against what we carry.
2. New or reworded rules → copy them in verbatim. Match their placement.
3. If they add a switcher, telemetry, a persona, or per-agent format sprawl → **skip it**,
   note why in the commit. look-first is `full` mode, two formats, no build.
4. If a change contradicts *Surface is not understanding* → keep both, and say so in the
   commit. Ours is the one addition; it does not get overwritten, but it also does not
   silently diverge.
5. Re-run the fidelity check (below). Update `README.md` credits if section names moved.
6. One commit per upstream. Message names the upstream commit you synced to.

## When you touch our section

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
K = key(pathlib.Path('CLAUDE.md').read_text())
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

## Three files stay identical

`CLAUDE.md`, `skills/look-first/SKILL.md`, `.openclaw/skills/look-first/SKILL.md` — same
body from `## Persistence` down. Edit `CLAUDE.md`, then regenerate the other two (they add
only frontmatter + a short intro; the openclaw one adds `homepage:`).

```
python3 -c "
import pathlib,re,hashlib
def b(p):
 t=pathlib.Path(p).read_text(); t=re.sub(r'^---\n.*?\n---\n','',t,flags=re.S)
 return hashlib.sha256(t[t.find('## Persistence'):].encode()).hexdigest()[:12]
for f in ['CLAUDE.md','skills/look-first/SKILL.md','.openclaw/skills/look-first/SKILL.md']:
 print(b(f), f)
"
```

Three identical hashes or it is not shipped.
