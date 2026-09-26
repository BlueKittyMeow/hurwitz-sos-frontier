# Conflicts and their disposition

Audit date: 2026-09-26. No unresolved contradictory numerical claim was admitted to the canonical ledger. Access and completeness gaps remain listed separately.

## C1. Integer optimality versus complex optimality — resolved

[Smith–Yiu Theorem (1), p.479](https://boletin.math.org.mx/pdf/2/37/BSMM%282%29.37.479-495.pdf) tabulates exact integer-coefficient composition numbers. Their upper constructions transfer to C. Their integer lower bounds do not. For example, the old integer diagonal entries for sizes 11 and 12 are 26, while the public complex construction in [Zhang–Zhu Theorem 1.1](https://arxiv.org/html/2605.00590v2) has length 18. These claims concern different coefficient fields and are compatible.

Disposition: construction data only from the integer tables; all complex lower bounds have separate authority. Both benchmark complex brackets are 17–18.

## C2. Real norm-preserving lower bounds versus nonsingular-map lower bounds — resolved

Shapiro Corollary 15.14, pp.337–338, concerns real norm-preserving formulas. Its entries cannot be moved wholesale into the complex ledger. Shapiro Theorem 12.21, p.245, concerns a different object, nonsingular skew-linear maps, and supplies lower bounds through Lemma 14.1, p.300. The real lower bound in Zhang–Zhu Corollary 1.2 likewise does not supply a complex lower bound.

Disposition: use the nonsingular-map table with a written Lam–Lam derivation; exclude the real-only lower table. [Public book text, pp.201–300](https://u.osu.edu/shapiro.6/files/2018/02/book3-2caati2.pdf), [pp.301–417](https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/c/5162/files/2018/02/book4-1hsrbaz.pdf).

## C3. Old construction tables versus published updates — resolved

Shapiro Chapter 13 Appendix C, pp.291–292, consolidates later construction work, including Yiu 1996 and Sánchez-Flores 1996. It improves several Smith–Yiu 1992 entries. The ledger uses the inspected updated table, followed by explicitly recorded elementary deductions from accepted public constructions. The old table is historical evidence, not a freshness guarantee. The later-construction comparison is in [RECENT_LITERATURE](RECENT_LITERATURE.md).

## C4. Nonsymmetric sigma table and apparent typo — quarantined outside scope

Shapiro Theorem 12.21 has an oriented sigma table; symmetry applies to the final bilinear composition number, not to sigma itself. The displayed entry sigma(12,4)=16 is inconsistent with the elementary construction at length 12. This apparent typo was not silently repaired or accepted. The only transcribed sigma block has both indices between 10 and 17, independently checked in all 64 positions.

Disposition: no canonical value depends on the questionable entry. Original-author clarification remains desirable; there is no unresolved canonical row from it.

## C5. Dugger–Isaksen BP source version — resolved with explicit version qualification

The older arXiv:math/0609301v1 Theorem 1.1 uses target `2m-1`. The [current author manuscript](https://pages.uoregon.edu/ddugger/etdq.pdf) uses `2m`, and its numerical example rules out `[11,15,18]`. Precise proof locators in this repository refer to that current manuscript. The [2008 journal metadata](https://doi.org/10.1017/S0305004108001205) is verified; the journal typesetting was not independently compared.

Disposition: pin the accessed author-text fingerprint and identify that text in every relevant source record. Never attribute the stronger statement to the old arXiv version.

## C6. Incorrect older divisibility equivalence — resolved

Dugger–Isaksen p.8 identifies an error in Davis's older Proposition 2.6: some relation types were omitted. Their corrected Proposition 2.15 is a necessary condition with a restricted index range.

Disposition: implement only the corrected range and necessity. An independent reviewer checked all 686 candidate certificates against the full relation matrix of Theorem 2.7; every emitted obstruction passed. No converse is used.

## C7. Metadata discrepancies — resolved or explicitly limited

- Zhang–Zhu v2 is dated **11 June 2026** by primary arXiv history. The May date belongs to v1. The ledger uses v2.
- Dugger–Isaksen's étale paper is from **2008**, not 2010.
- Lam–Randall's original 1995 proceedings article has publisher-deposited pagination 137–160, while Shapiro's bibliography gives 129–152. This is a bibliographic discrepancy. The original article is not numerical authority in this release because its full table was not accessed. Its DOI is [10.1090/conm/188/02239](https://doi.org/10.1090/conm/188/02239).
- Source upload and crawl dates were not treated as publication dates. Hrubeš's journal successor is genuinely from 2026; its available author manuscript is dated 2024.

## Private comparisons

Private sources were not opened for numerical comparison. Accordingly, this audit makes no claim about the contents or correctness of any previous internal assumption. Its public comparison is with the cited classical tables. Private closures for sizes 11 or 12 have no role in the data.
