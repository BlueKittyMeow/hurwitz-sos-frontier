# Hurwitz SOS Frontier

Public, source-cited lower bounds, upper bounds, and exact values for bilinear sums-of-squares formulas over **C**.

**Initial snapshot: 26 September 2026.** The canonical ledger covers all 528 pairs with `1 <= r <= s <= 32`. It uses inspected public theorems and construction tables, together with explicit elementary deductions. It is a public literature index, not an original-results repository. “Frontier” means the strongest bounds found in the audited sources and stated deductions; the [known gaps](audits/KNOWN_GAPS.md) remain part of this release.

## Definition and field convention

A formula of type **[r,s,n] over C** is a polynomial identity

\[
 (x_1^2+\cdots+x_r^2)(y_1^2+\cdots+y_s^2)
 =z_1(x,y)^2+\cdots+z_n(x,y)^2,
\]

where each `z_k` is bilinear in the two input vectors and has complex coefficients. These are ordinary algebraic squares: **no complex conjugation**. Define `N_C(r,s)` as the least positive output dimension `n` for such an identity. Zero output forms are allowed, so existence is preserved by target padding.

Swapping the two inputs proves `N_C(r,s) = N_C(s,r)`. The CSV stores only `r <= s`; provenance retains the orientation of each source statement. Real, integer, finite-field, and rational-function problems have different conventions and are not interchangeable with this one.

## Read the frontier

- [Diagonal frontier](generated/diagonal.md)
- [Exact cells](generated/exact_cells.md)
- [Cells with unequal bounds](generated/open_cells.md)
- [Selected rectangles](generated/rectangular.md) and [all cells](generated/all_cells.md)
- [Sources and publication status](generated/sources.md)
- [Inspectable bound derivations](generated/derivations.md)

Every displayed bound links to its own proof and source record. A cell is exact only when independently supported lower and upper bounds agree. An unequal bracket means that this audit does not determine the exact value; it does not certify that the entire literature leaves it open. An absent cell has not been audited. No value is filled by interpolation.

The full initial window is possible because Smith–Yiu's small-input construction theorem and the inspected classical tables cover it. The release contains **270 exact cells and 258 bounded cells**, with no unresolved conflicting numerical row accepted. This is not a claim of exhaustive coverage outside the window.

The benchmark cells `(11,11)` and `(12,12)` both have public bracket **17–18**. The lower authority is Shapiro's nonsingular-map table plus the Lam–Lam lemma. The upper authority is the **public preprint** [Zhang–Zhu v2](https://arxiv.org/html/2605.00590v2), with a recorded restriction for `(11,11)`. No exact value is inferred from the construction.

## Source and derivation policy

Use externally accessible mathematical sources. Peer-reviewed papers, scholarly monographs, proceedings, public preprints, and theses retain their distinct publication statuses. Primary statements are preferred; a monograph table is identified as such when the original citation chain could not be fully inspected. Repeated secondary claims are not evidence.

Integer or real constructions can give complex upper bounds by scalar extension. Real lower bounds require a valid transfer theorem. The Lam–Lam lemma transfers a complex formula to a **nonsingular real bilinear map**, so applicable nonsingular-map obstructions can be used. It does not transfer every obstruction to norm-preserving real formulas. This distinction excludes Shapiro's real-only lower table and the real lower bound in Zhang–Zhu from the complex ledger.

Some bounds specialize published theorem families; others restrict source variables or concatenate outputs in a direct sum. Each is labeled derived and proved in a few lines. The finite closure operations and their limits are documented in [SOURCE_AUDIT](audits/SOURCE_AUDIT.md). They are arithmetic consequences of public results, without claims of new theorems or priority.

**Private lab amendments, unpublished theorems, private branches, and internal numerical claims are excluded.** No private numerical material was consulted to construct this release. Source PDFs are linked, not redistributed.

## Data and reproducibility

- `data/complex_frontier.csv`: canonical bounds, separate lower/upper source IDs, status, provenance, date, and notes.
- `data/sources.yaml`: stable bibliography IDs, public URLs, field interpretation, and exact locators.
- `data/derivations.yaml`: proof graph, input results, operations, and integer witnesses.
- `data/source_tables.yaml`: transcribed source data, including the nonsymmetric sigma table.
- `schemas/`: JSON Schemas for each canonical dataset.
- `audits/`: conflicts, source coverage, freshness, gaps, and independent review.

`exact` is a Boolean encoded as `true` or `false`. Multi-valued CSV fields use semicolons. `lower_status` and `upper_status` give publication statuses, including all source ancestry for a derived bound. `audit_status=audited` means the recorded bound and provenance were checked; it is not a guarantee of global literature completeness. The UTC timestamp denotes the audit day, at day precision.

Python 3.12 was used for the freeze:

```sh
python -m pip install -r requirements.txt
python scripts/build.py
python scripts/validate.py
python scripts/verify_zhang_zhu.py
python scripts/independent_check.py
python scripts/check_later_families.py
python scripts/generate.py
python scripts/generate.py --check
python -m unittest discover -s tests -v
```

The builder and validators work offline. They check schemas, duplicate cells, ordering and symmetry, source IDs, exactness, inequality consistency, an acyclic derivation graph, arithmetic witnesses, direct sums, restrictions, and deterministic regeneration. The explicit Zhang–Zhu construction is checked with exact Gaussian integers.

## Corrections, reuse, and citation

Please open an issue or pull request with a primary source, exact locator, field convention, and separate justification for each changed bound. See [CONTRIBUTING](CONTRIBUTING.md). We preserve material conflicts and explain their resolution.

For a reproducible citation, use the repository URL together with the release tag and full commit SHA. This snapshot is an AI-assisted literature audit with independent agent checks and parent adjudication; it has not undergone external human peer review. Review coverage is documented in [INDEPENDENT_REVIEW](audits/INDEPENDENT_REVIEW.md).

Original repository code, data compilation, and documentation are released under the [MIT license](LICENSE). Cited works retain their own copyrights and licenses. Mathematical facts remain reusable independently of this compilation.
