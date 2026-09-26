# Initial public snapshot: v0.1.0

Audit through 26 September 2026. The tag identifies the frozen Git snapshot; the CSV/YAML fingerprints are in [FREEZE.json](FREEZE.json).

- 528 canonical complex cells: 270 exact, 258 bounded, zero unresolved canonical rows.
- 15 source records: 11 peer-reviewed journal papers, two proceedings papers, one scholarly monograph, one public preprint.
- Seven sources supply numerical bounds: five journal papers, one monograph, one public preprint.
- Numerical authority dates range from Antoniano–Gitler (1984) to Zhang–Zhu v2 (11 June 2026). Adams (1962) is the oldest separately audited historical source.
- 1,056 derivation records; all reviewed. Schema, arithmetic, exactness, symmetry, provenance, deterministic regeneration, independent checks, and eight deliberate-corruption tests passed before publication.

## Required benchmarks

Every bracket below links to its lower and upper certificates. All use ordinary complex algebraic squares.

| Cell | Lower | Upper | Exact? |
|---|---:|---:|:---:|
| (8,8) | [8](../generated/derivations.md#l-8-8) | [8](../generated/derivations.md#u-sy-8-8) | yes |
| (9,9) | [16](../generated/derivations.md#l-9-9) | [16](../generated/derivations.md#u-sy-9-9) | yes |
| (10,10) | [16](../generated/derivations.md#l-10-10) | [16](../generated/derivations.md#u-table-smith-yiu-1992-10-10) | yes |
| (11,11) | [17](../generated/derivations.md#l-11-11) | [18](../generated/derivations.md#u-d0002) | no |
| (12,12) | [17](../generated/derivations.md#l-12-12) | [18](../generated/derivations.md#u-zz-12-12) | no |
| (13,13) | [19](../generated/derivations.md#l-13-13) | [28](../generated/derivations.md#u-table-smith-yiu-1992-13-13) | no |
| (14,14) | [23](../generated/derivations.md#l-14-14) | [32](../generated/derivations.md#u-table-smith-yiu-1992-14-14) | no |
| (16,16) | [23](../generated/derivations.md#l-16-16) | [32](../generated/derivations.md#u-table-smith-yiu-1992-16-16) | no |
| (17,18) | [32](../generated/derivations.md#l-17-18) | [32](../generated/derivations.md#u-table-shapiro-2000-17-18) | yes |
| (18,18) | [32](../generated/derivations.md#l-18-18) | [50](../generated/derivations.md#u-table-shapiro-2000-18-18) | no |
| (20,20) | [32](../generated/derivations.md#l-20-20) | [56](../generated/derivations.md#u-table-shapiro-2000-20-20) | no |

## Conflicts and comparisons

Integer optimality and real norm-preserving lower bounds were separated from complex claims. The BP source-version discrepancy and incorrect older divisibility equivalence were resolved by using the inspected current author text and its corrected necessary criterion. An apparent sigma-table typo outside the transcribed block was quarantined. Full details: [CONFLICTS](CONFLICTS.md).

The public benchmark brackets at (11,11) and (12,12) are both 17–18, not exact closures. Their classical integer upper construction length was 26. Private assumptions were not inspected, so this release makes no private comparison. Elementary public-source sums also yield diagonal upper bounds 63 at size 21, 66 at size 22, and 114 at sizes 31 and 32; their proof chains and preprint ancestry are explicit.

## Review and remaining gaps

Separate agents checked seven exact cells, eight bounded cells, the latest construction, every transcribed table entry, every restriction-dependent bound, and all direct sums. The parent adjudicated the evidence. This remains an AI-assisted audit without external human peer review. See [INDEPENDENT_REVIEW](INDEPENDENT_REVIEW.md).

Original Lam–Randall and full 1996 construction sources, final journal typesetting for the BP paper, and exhaustive later/topological literature coverage remain gaps. The canonical claim is the strongest supported bound found in the audited sources and recorded finite deductions. See [KNOWN_GAPS](KNOWN_GAPS.md).

**Private lab amendments and unpublished numerical claims were excluded.** No copyrighted source PDFs are distributed. Original repository code, compilation, and documentation use the MIT license.
