# Roadmap

This file records follow-up work for the public **Hurwitz SOS Frontier** after the frozen `v0.1.0` release.

The release itself remains immutable. Corrections and coverage improvements belong in later commits/releases with explicit provenance.

## First-pass post-release audit

A separate spot audit of `v0.1.0` checked the repository architecture, selected numerical rows, derivation chains, independent-review machinery, release/tag integrity, and CI state.

Findings:

- No confirmed numerical error was found in `v0.1.0`.
- The release tag resolves to the documented frozen commit.
- Both GitHub Actions validation runs on the frozen commit passed.
- Selected diagonal and rectangular rows were traced through their actual derivation records rather than only the generated tables.
- The apparently large count of exact cells is structurally plausible: most exact rows lie in the classical small-input regime covered by the Smith–Yiu theorem, with a much smaller set of exact cells beyond it.
- The clean-room reconstruction corrected at least one stale secondary numerical assertion encountered during comparison rather than reproducing it. This reinforces the value of primary-source provenance.
- The main remaining risk is **literature coverage**, not arithmetic or schema integrity.

The repository should therefore treat `v0.1.0` as a supported initial snapshot, not as a completed literature census.

## Priority for v0.2: deepen the 1–32 literature audit

### 1. Complete the Lam–Randall / geometric-dimension lower-bound chain

Highest priority.

Locate and inspect the original/full texts behind the geometric-dimension and sectioning results that can imply nonsingular-bilinear-map lower bounds, especially:

- Kee Yuen Lam and Duane Randall, **“Geometric dimension of bundles on real projective spaces,”** in *Homotopy Theory and Its Applications* (Cocoyoc, 1993), Contemporary Mathematics 188, AMS, 1995, pp. 137–160.
- Related Lam–Randall periodicity/geometric-dimension papers referenced by the above source or by Shapiro.
- Earlier geometric-dimension inputs that are actually used in the numerical chain.

Goal:

- reconstruct every cellwise consequence for `1 <= r <= s <= 32`;
- record exact theorem/page locators;
- distinguish direct source statements from deductions;
- test whether any current lower bounds improve.

Do not infer complex SOS lower bounds from real geometric results without the required transfer theorem.

### 2. Complete the 1996 upper-construction primary-source chain

Obtain and inspect the full papers, rather than relying only on Shapiro's later consolidation:

- Paul Y. Yiu, **“Some upper bounds for composition numbers,”** *Boletín de la Sociedad Matemática Mexicana* (3) 2 (1996), 65–77.
- Adolfo Sánchez-Flores, **“A method to generate upper bounds for the sums of squares formulae problem,”** *Boletín de la Sociedad Matemática Mexicana* (3) 2 (1996), 79–92.

Also inspect relevant predecessor/construction sources when locally available, including:

- Paul Yiu, **“Composition of Sums of Squares with Integer Coefficients,”** in *Deformations of Mathematical Structures II* (1994), pp. 7–100.
- David Romero, **“New constructions for integral sums of squares formulae,”** *Boletín de la Sociedad Matemática Mexicana* (3) 1 (1995).

Goal:

- reproduce the actual construction/juxtaposition algorithms where feasible;
- compare their complete consequences against the current 1–32 upper frontier;
- record whether Shapiro's Appendix C table fully subsumes them inside the window;
- preserve source-level provenance even when no numerical row changes.

### 3. Build a literature-disposition matrix

Every plausibly relevant source found in searches should receive an explicit disposition, for example:

- `numerical authority`
- `subsumed by later authority`
- `wrong field / no valid transfer`
- `context only`
- `construction family checked, no improvement in window`
- `inaccessible / pending acquisition`
- `not yet evaluated`

Candidate sources for explicit disposition include:

- Paul Y. H. Yiu, **“Quadratic forms between spheres and the non-existence of sums of squares formulae,”** *Math. Proc. Cambridge Philos. Soc.* 100 (1986), 493–504.
- Carlos Domínguez and Kee Yuen Lam, **“Nonsingular bilinear maps revisited,”** *Proc. Roy. Soc. Edinburgh Sect. A* 151 (2021), with arXiv:1811.03200.
- Pavel Hrubeš, Avi Wigderson, and Amir Yehudayoff, **“Non-commutative circuits and the sum-of-squares problem,”** *J. Amer. Math. Soc.* 24 (2011), 871–898.
- Pavel Hrubeš, Avi Wigderson, and Amir Yehudayoff, **“An asymptotic bound on the composition number of integer sums of squares formulas,”** *Canad. Math. Bull.* 56 (2013), 70–79.

These may or may not change a canonical complex cell. Recording the disposition prevents repeated rediscovery.

### 4. Forward/backward citation audit

For every numerical-authority source in `data/sources.yaml`:

- inspect cited predecessors that could contain stronger tables or exceptional cases;
- inspect later papers that cite the source and may improve a bound;
- record search date, query family, and disposition;
- prioritize citations touching dimensions 10–32.

The goal is not to prove absence of later work, but to make the coverage claim inspectable.

### 5. Separate derivation verification from literature-coverage confidence

Consider extending the schema so readers cannot confuse a verified derivation with an exhaustive literature claim.

Possible fields:

- `derivation_verified`
- `source_statement_verified`
- `literature_coverage_status`

Suggested coverage values:

- `partial`
- `strong`
- `targeted-complete`
- `exhaustive-not-claimed`

The exact vocabulary should remain small and documented.

### 6. Re-audit all benchmark diagonals after new source ingestion

At minimum rerun primary-source review for:

`(10,10)`, `(11,11)`, `(12,12)`, `(13,13)`, `(14,14)`, `(16,16)`, `(17,17)`, `(18,18)`, `(20,20)`, `(24,24)`, `(32,32)`.

Preserve lower and upper provenance independently.

## Later work

### Expand beyond 32 only after deepening the initial window

A future release may extend the canonical complex window to 64 or beyond, especially because several historical construction papers explicitly discuss that range.

Do not expand merely for row count.

First ensure:

- the major 1–32 lower-bound citation chains are recovered;
- the 1990s construction algorithms have been audited;
- the literature-disposition matrix exists;
- field-transfer policy is stable;
- validation remains deterministic.

### Other fields

Separate ledgers may eventually cover:

- real coefficients;
- algebraically closed fields of positive characteristic;
- finite fields;
- integer-coefficient composition numbers.

Do not merge these into the complex ledger.

### External review and community corrections

Useful future improvements include:

- review by human specialists in composition formulas, nonsingular bilinear maps, and projective-space topology;
- GitHub issues/PRs for missing sources and corrected locators;
- release notes that distinguish numerical changes from provenance-only improvements.

## Acquisition policy

The public repository should continue linking to external sources rather than redistributing copyrighted PDFs.

A private authenticated research library may be used for source inspection, provided every canonical public claim cites a publicly identifiable scholarly source and enough bibliographic metadata for another researcher to locate it.

## Release discipline

- Keep `v0.1.0` frozen.
- Make source/provenance improvements on `main`.
- Issue `v0.2.0` only after a coherent coverage pass and independent review.
- Every changed numerical row must identify the prior value, new value, source, derivation, and review.
- Provenance-only corrections should be recorded even when no number moves.

The long-term goal is not merely a large table. It is a durable, inspectable public map of what the literature actually supports.
