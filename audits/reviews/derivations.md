# Independent derivation review

Date: 2026-09-26. Verdict: **PASS for the reviewed snapshot; no numerical or graph defect found.**

Reviewer used `scripts/independent_check.py`, written independently without importing or reading the repository builder/validator. Snapshot: 528 canonical cells, 1,056 derivations, 15 source records. The script checks every derivation and both sides of every row. It verifies dependency existence, acyclicity, exact integer arithmetic, source aggregation, publication statuses, and agreement between each row and its cited derivations. Maximum dependency depth: 5.

## Complete operation coverage

| Operation | Count checked |
|---|---:|
| Upper explicit small-input construction specialization | 252 |
| Upper scalar extension of transcribed construction table | 229 |
| Upper direct Zhang–Zhu statement | 1 |
| Upper source restriction | 4 |
| Upper direct sum | 42 |
| Lower rank specialization | 83 |
| Lower explicit Hopf/Xie specialization | 316 |
| Lower sigma restriction and Lam–Lam transfer | 27 |
| Lower BP2 restriction and specialization | 98 |
| Lower axial obstruction and Lam–Lam transfer | 4 |

All **129 restriction-labelled records** were checked: 4 upper, 27 sigma lower, 98 BP2 lower. Of these, **109 involve a genuine decrease in source dimensions**: 4 upper, 20 sigma lower, 85 BP2 lower. The other 20 lower records use the same source cell, sometimes with orientation exchanged. Every restriction-dependent best bound in this snapshot is covered.

## Mathematical checks

Upper restrictions preserve output length and reduce both ordered source dimensions. All four have exactly one valid input. All 42 direct sums share one source dimension after the explicitly recorded swaps, split the other into the recorded positive block sizes, and add output dimensions exactly. The union of leaf source IDs matches each resulting record. Concatenating output bilinear forms is a valid construction over C. No unrestricted tensor-product inference is used.

All 252 small-input construction values were independently recomputed by searching the Hopf parity condition, within the theorem's r<=9 range. All 229 table leaves match their cited source-table records. Original construction-table transcription accuracy is covered by the separate table review, rather than being claimed as freshly re-read in this review.

The complete oriented 10..17 sigma square was independently manually entered from Shapiro Theorem12.21's public text: all 64 source-table entries match. Every selected sigma witness is a valid restriction, has the correct orientation/value, and transfers through the Lam–Lam real-part argument. This does not transfer positive-definite real formula obstructions.

All 98 BP2 witnesses obey max(a,b)<m<=a+b and the corrected Proposition2.15 index bound. Binomial integers, required powers of two, nonzero remainders, input restrictions, and resulting lower=2m+1 were independently checked. All remaining lower witnesses were checked against their exact parity/rank/Xie/axial arithmetic. Target padding correctly turns rejection of lower-1 into the stated bound.

## Requested large upper bounds

- (21,21)<=63: [9,21,29] plus [12,21,34]; the latter is [12,9,16] plus Zhang–Zhu [12,12,18]. Thus29+16+18=63.
- (22,22)<=66: [10,22,30] plus [12,22,36]; the latter combines a [12,10,18] restriction with [12,12,18]. Thus30+18+18=66.
- (31,31)<=114: [9,31,32] plus [22,31,82]; the latter is [10,31,32] plus [12,31,50], and50=18+32 from [12,11,18] and [12,20,32]. Thus32+32+18+32=114.
- (32,32)<=114: two [10,32,32] blocks plus [12,32,50], where50=18+32 from [12,12,18] and [12,20,32]. Thus32+32+18+32=114.

These are explicit consequences of public constructions, not private authority. They require the recorded derived labels and individual DAG, which are present.

## Status and version checks

All row source IDs exist and exactly match the relevant derivation. Row publication-status sets match source records, including mixed book/journal/preprint ancestry. Zhang–Zhu is correctly identified as public preprint arXiv2605.00590v2 dated2026-06-11. The 2008 Dugger–Isaksen record explicitly warns that its used text is the current author manuscript with target2m, while linked arXivv1 has target2m-1. Numerical locators refer to the used manuscript, so no silent version substitution occurs. The field is consistently C; all rows satisfy lower<=upper and exact iff equal. No duplicate canonical cells exist.

Known publication and access gaps remain visible; this review does not turn those into completed primary-source audits or claim global literature completeness.

## Reproducible snapshot SHA256

- complex_frontier.csv: `80ae59db75ee805f870fdc37a1b4f0658f2da1eee96d366d2046b1c570eedb95`
- derivations.yaml: `bbac528653e654b34e7110781194691cc7ab0a4c2525647b007ba81b6c3d3a04`
- source_tables.yaml: `235fbe880340b27cfe6a5ca659b2237a67f785abcc093435ed417452c85925ac`
- sources.yaml: `6a0c240d8bc1a6f1ed0db4ff5ce5272289945cfbc8ab446301a930dc9e512433`

Raw execution report: `reviewer scratch execution output`.
