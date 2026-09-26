# Independent release review: numerical frontier

Reviewer role: public-literature freshness auditor, independently reviewing the parent's generated ledger. Review date: 2026-09-26. No repository files were edited. No private repositories, numerical claims, or unpublished lab content were consulted.

## Verdict

PASS for the stated source-backed ledger and recorded elementary derivations. Reviewed snapshot has **528 complex cells: 270 exact, 258 bounded, zero unresolved**. All **1,056 derivation records** passed the independent checks described below. This is not a claim of exhaustive literature coverage or independent reproving of every cited published theorem.

The separate review program `reviewer scratch validator (not retained)` reads the release CSV/YAML but does not import or execute its build or validation modules. It independently calculates certificate arithmetic, dimensions, orientations, source-table equality, DAG integrity, and row-to-derivation consistency. Machine output is `reviewer scratch execution output`.

## Primary text used

- Smith and Yiu (1992), Theorem(1), p479; Proposition(7), p484; Theorem(9), p485: https://boletin.math.org.mx/pdf/2/37/BSMM%282%29.37.479-495.pdf . The numerical table and small-input construction were independently read through primary web PDF extraction. A local download returned HTTP406, so it was not used as a PDF. All28 canonical entries of the p479 table were separately transcribed and matched. Only construction/existence transfers from integers to C; integer optimality was not used as a complex lower bound. The small-input theorem was checked independently using the XOR sumset cardinality defining r o s.
- Shapiro (2000), Theorem12.21 p245, AppendixC p292, Lam–Lam Lemma14.1 p300: https://u.osu.edu/shapiro.6/files/2018/02/book3-2caati2.pdf . Rendered and inspected both table pages. All248 p292 upper entries matched extracted primary text; all64 oriented sigma entries for 10<=r,s<=17 matched a fresh manual transcription. Sigma is treated as oriented. The transfer sends complex output U+iV to the nonsingular real map U and preserves target dimension. It does not assert a real norm-preserving formula.
- Dugger–Isaksen, Hopf theorem1.2 p943: https://annals.math.princeton.edu/wp-content/uploads/annals-v165-n3-p05.pdf . Its binomial-parity obstruction applies to C.
- Dugger–Isaksen, final author manuscript, Theorem1.1 and corrected Definition2.13/Proposition2.15: https://pages.uoregon.edu/ddugger/etdq.pdf . Reviewed the truncation k<=d-floor((d+1)/3); the release uses the valid necessary condition, without assuming the false converse discussed in the paper.
- Xie (2014), Theorem1.1 p195: https://www.maths.tcd.ie/EMIS/journals/DMJDMV/vol-19/06.pdf (source PDF also available among parent-provided public downloads). Reviewed the phi count, orientation, exponent, and index bounds.
- Antoniano–Gitler (1984), Theorem1.6 and pp7–9 exception analysis, https://www.boletin.math.org.mx/pdf/2/29/BSMM%282%29.29.5-9.pdf (primary downloaded text inspected). Reviewed how projective dimensions give the four recorded axial lower bounds; all have the larger projective source dimension >=16, outside the exceptional cases.
- Zhang–Zhu arXiv2605.00590v2, Theorem1.1 and §3.1: https://arxiv.org/html/2605.00590v2 . In the earlier independent audit I transcribed equation(3.2) and checked all20,736 polarized coefficient equations, with no failures. Version date is June11,2026.

## Required exact-cell spot checks

Seven independent exact-cell checks, with both sides supported:

| Cell | Value | Lower authority / certificate | Upper authority |
|---|---:|---|---|
| (1,1) | 1 | Rank specialization | Smith–Yiu Thm9 |
| (2,2) | 2 | Rank specialization | Smith–Yiu Thm9 |
| (4,4) | 4 | Rank specialization | Smith–Yiu Thm9 |
| (8,8) | 8 | Rank specialization | Smith–Yiu Thm9 |
| (9,9) | 16 | Hopf at n15, i7; odd binomial | Smith–Yiu Thm9 |
| (10,10) | 16 | Hopf at n15, i6; odd binomial | Smith–Yiu p479 |
| (17,18) | 32 | Hopf at n31, i15; odd binomial | Shapiro p292 |

The lower argument excludes the immediately preceding output dimension. Padding therefore excludes every smaller dimension. No table's “optimal” annotation substitutes for a complex lower-bound certificate.

## Required bounded-cell spot checks

Eight independent checks:

| Cell | Bracket | Lower certificate | Upper authority |
|---|---|---|---|
| (11,11) | 17–18 | Restrict to oriented sigma(10,11)=17, then Lam–Lam | Zhang–Zhu restriction |
| (12,12) | 17–18 | Same sigma restriction | Zhang–Zhu Thm1.1 |
| (13,13) | 19–28 | sigma(10,13)=19 | Smith–Yiu p479 |
| (14,14) | 23–32 | sigma(13,14)=23 | Smith–Yiu p479 |
| (16,16) | 23–32 | sigma(11,16)=23 | Smith–Yiu p479 |
| (18,18) | 32–50 | Hopf n31,i14 | Shapiro p292 |
| (20,20) | 32–56 | Hopf n31,i12 | Shapiro p292 |
| (24,24) | 37–72 | Restrict to [21,23,36]; a10,b11,m18,d3,k2; binomial(19,9)=92378 is not divisible by4 | Shapiro p292 |

In particular, (11,11) and (12,12) remain bounded. No claim of exact18 was accepted.

## Every restriction and direct-sum derivation

All **four upper source-restriction nodes** passed:

- (12,12,18) -> (11,12,18).
- (11,12,18) -> (11,11,18).
- (11,12,18) -> (10,12,18).
- (10,12,18) -> (10,11,18).

Setting unused input variables to zero preserves the polynomial identity, field, and target dimension. This accounts for every upper restriction node retained in the provenance graph.

All **42 direct-sum nodes** passed independent tests of both oriented input dimensions, common unsplit input, split sizes, output-length addition, source-ID inheritance at row level, and acyclicity. Concatenating outputs proves the stated bound because the two input-block norms add. Input nodes are checked recursively, including intermediate nodes that differ from the final cell's best bound.

All **27 sigma lower restriction certificates** passed target/source dimension checks in at least one orientation and matched the oriented primary table. All **98 BP2 lower restriction certificates** passed dimension, theorem-hypothesis, sequence-index, binomial, modulus, and resulting-lower-bound checks. Input dimensions are 2a+1 and 2b+1 and rejected output dimension is2m; the resulting lower bound is2m+1. Neither orientation nor target padding was reversed.

Other validated lower records: **83 rank**, **288 Hopf**, **28 Xie**, **4 axial**. Other upper records: **252 small-input constructions**, **229 table constructions**, **1 Zhang–Zhu direct construction**. Every row's stored lower and upper values match its respective derivation output. Every exact flag equals the truth of lower==upper. Canonical ordering and unique cell coverage passed.

## Independent freshness check

Previously enumerated 19,607 instances from Lenzhen–Morier-Genoud–Ovsienko2011 and Hu–Huang–Zhang2018 construction families, including stated exceptions, for family parameter n=4..32. Direct restrictions/symmetry produced no improvement over Shapiro's248 p292 cells. This is finite family checking, not a proof that arbitrary combinations of all public constructions yield no improvement. See `audits/RECENT_LITERATURE.md` and `scripts/check_later_families.py`.

## Snapshot fingerprints

- complex_frontier.csv SHA256: `80ae59db75ee805f870fdc37a1b4f0658f2da1eee96d366d2046b1c570eedb95`
- derivations.yaml SHA256: `bbac528653e654b34e7110781194691cc7ab0a4c2525647b007ba81b6c3d3a04`
- source_tables.yaml SHA256: `235fbe880340b27cfe6a5ca659b2237a67f785abcc093435ed417452c85925ac`

## Findings and limits

No incorrect numerical claim or derivation was found in this snapshot. All numerical origins resolve to public primary literature or explicit elementary deductions. Original Lam–Randall and complete1996 construction proofs were not independently read; Shapiro's published monograph is the authority used for those table values. This review does not certify remote publication state, Git history, code licensing, or literature completeness. Private lab amendments were excluded.
