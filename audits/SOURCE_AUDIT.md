# Source audit and acceptance method

Audit date: 2026-09-26. Scope: ordinary complex bilinear composition formulas, source dimensions through 32.

## Numerical authorities

| Source ID | Material inspected | Accepted role |
|---|---|---|
| `smith-yiu-1992` | Theorems (1), (2), (9), Proposition (7), construction sections | Integer construction upper bounds; never integer optimality as a complex lower bound |
| `shapiro-2000` | Theorem 12.21, Lemma 14.1, Appendix C, real-only comparison table | Oriented nonsingular-map lower table plus valid complex transfer; updated integer upper table |
| `dugger-isaksen-2007` | Theorem 1.2 and field discussion | Hopf parity lower certificates in characteristic other than two |
| `dugger-isaksen-2008` | Current author manuscript Theorems 1.1/2.7, Corollary 2.10, Definition 2.13, Proposition 2.15 | Corrected BP2 divisibility obstruction, with explicit integer witnesses |
| `xie-2014` | Theorem 1.1 and Remarks 1.1–1.3 | Hermitian K-theory obstruction, both input orientations |
| `antoniano-gitler-1984` | Entire paper, especially Theorem (1.6) and all exception cases | Axial-map inequality after explicit Lam–Lam transfer |
| `zhang-zhu-2026` | Pinned v2 theorem, coefficient criterion, explicit array | Public preprint construction, checked in exact arithmetic |

Exact bibliographic details, public URLs, field conditions, and locators are in the [source index](../generated/sources.md). Author-hosted PDFs were downloaded into temporary storage for inspection and are not included in Git.

## Required historical and modern coverage

Shapiro's table pages and the Smith–Yiu table were rendered and inspected, then independently checked. The construction table in Shapiro incorporates the important 1996 updates. Full original citation-chain access remains a recorded gap.

The Hopf–Stiefel condition is accepted through Dugger–Isaksen's primary arbitrary-field theorem. Adams's primary vector-field theorem was read. Shapiro Chapter 12 presents its K-theory application and Atiyah's method; Xie provides the applicable stronger field-uniform theorem used here. The audit does not confuse a complex formula with a nonsingular complex bilinear map.

Lynn's algebraically closed field-comparison theorems were read; they do not supply a small numerical table and do not equate real and complex existence. Hrubeš's finite construction and asymptotic theorem were read, and the 2026 journal successor was located. Big-O estimates were not turned into invented cell values. Later 2011/2018 integer construction families, 2017 doubling work, and 2026 complexity papers were checked for relevance; see [RECENT_LITERATURE](RECENT_LITERATURE.md).

## Transcription and field transfer

`source_tables.yaml` preserves 28 upper entries from Smith–Yiu p.479, 248 upper entries from Shapiro p.292, and 64 **oriented** sigma entries from Shapiro p.245. These are source assertions, not the final frontier. Their larger historical values may be superseded in the CSV.

The small-input theorem covers the remaining 252 cells with `r <= 9`. Its value is evaluated exactly through the equivalent Hopf condition. Thus the rectangular window is source-covered; no interpolation was needed.

For an integer construction, scalar extension `Z -> C` is recorded as a derivation. For a nonsingular-map lower bound, writing a complex output as `U+iV` gives `||U||^2 = ||x||^2 ||y||^2 + ||V||^2` on real inputs. Hence `U` is nonsingular, justifying Shapiro's Lam–Lam transfer with the same target dimension. This does not imply a real norm-preserving formula.

## Elementary closure and its limits

The upper seeds are the inspected integer tables, the small-input theorem, and Zhang–Zhu's `[12,12,18]`. Within `1 <= r <= s <= 32`, the builder repeatedly applies:

1. Source restriction by setting unused variables to zero.
2. Symmetry when an input construction is used in the opposite orientation.
3. Direct sum along one input: split that input into disjoint blocks, hold the other fixed, and concatenate the output forms.

Every improvement stores its actual input derivations as immutable nodes. No cyclic reference to a later improved cell is possible. The resulting graph has depth at most five. The selected lower bound is the maximum among rank, Hopf, Xie, applicable sigma-table restrictions, corrected BP2 specializations/restrictions, and the applicable axial-map inequality. Target padding is included in each nonexistence certificate where needed.

These operations yield some tighter bounds than the source tables literally print. They are labeled derived and do not assert new theorem priority. No unrestricted tensor-product rule is used. More elaborate construction families and arbitrary closures are outside the builder's claim.

## Parent adjudication and provenance boundary

The parent read the accepted primary statements and field conventions, inspected the table pages, reproduced the arithmetic and construction verification, and reconciled the independent reports. All accepted numerical leaves have a public source. Discovery and review agents were instructed to use public sources only. The release was created in an initially empty separate directory; no private numerical files or proof content were imported.

Review details, including every restriction-dependent row, are in [INDEPENDENT_REVIEW](INDEPENDENT_REVIEW.md). Conflicts were retained in [CONFLICTS](CONFLICTS.md). Remaining limitations are part of the frozen release in [KNOWN_GAPS](KNOWN_GAPS.md).
