# Independent lower-bound review — 2026-09-26

Reviewer: classical-source auditor, independent of the large-diagonal scout and frontier builder. No repository edits or private sources used.

## Verdict

PASS the proposed complex lower bounds N_C(25,25)>=38, N_C(26,26)>=39, N_C(32,32)>=48. PASS the current builder's BP specialization. No numerical correction required.

## Antoniano–Gitler source audit

E. Antoniano and S. Gitler, *Axial maps and cross-sections*, Bol. Soc. Mat. Mexicana(2)29(1)(1984),5–9. Primary peer-reviewed journal.

https://www.boletin.math.org.mx/pdf/2/29/BSMM%282%29.29.5-9.pdf

Read all five pages; visually inspected pp6 and9. Theorem1.6 p6 assumes projective dimensions m<=n<=k and gives n<2(k-m), subject to finite exceptions. Its proof divides exceptions into cases I–III. CaseII is eliminated entirely. CaseI exceptions have binary exponent<=3, hence n<=15. CaseIII exceptions also have exponent<=3: p9 explicitly excludes exponents4 and5, while the preceding lemmas exclude larger exponents. Thus no exception has larger projective source dimension>=16. The paragraph before Theorem1.6 independently states that diagonal exceptions have n<=15. Source typographical errors in some proof displays do not alter these explicitly stated ranges; the theorem and case conclusions agree.

## Transfer and arithmetic certificate

Use Shapiro2000 Lemma14.1 p300. For complex output z=U+iV on real input, ||U||²=||x||²||y||²+||V||², so U is nonsingular bilinear over R. Projectivizing U gives an axial map RP^(r-1) x RP^(s-1) -> RP^(N-1): each fixed nonzero input gives an injective linear map on the other factor, hence a nontrivial projective restriction.

For canonical2<=r<=s with s>=17, set(m,n,k)=(r-1,s-1,N-1). Rank gives k>=n. The exception audit above applies, so

    s-1 < 2((N-1)-(r-1)) = 2(N-r).
    N >= r + ceil(s/2).

This general rectangle bound is valid; retain max(s,r+ceil(s/2)) with the rank bound. For r=1 use rank directly.

Diagonal specializations:

- (25,25): reject N=37 because24<24 is false; lower38.
- (26,26): reject N=38 because25<24 is false; lower39.
- (32,32): reject N=47 because31<30 is false; lower48.

Appending zero output forms reduces rejection of all smaller N to rejection at the displayed target. For an especially conservative implementation, restricting the family to diagonals q>=18 is sufficient for the three requested improvements.

## BP primary-source and code review

Dugger–Isaksen author-final manuscript https://pages.uoregon.edu/ddugger/etdq.pdf ; local audited PDF `temporary public-source download (not distributed)`.

Read Theorem1.1 p3, Theorem2.7 p6, Corollary2.10 p7, Definition2.13 and Proposition2.15 p8; visually inspected p8. The builder uses the corrected condition, not the invalid Davis equivalence discussed there. For each(a,b,m), its range max(a,b)<m<=a+b and d=a+b-m are correct. Its formula

    S_k = binomial(m+floor(k/2), a-ceil(k/2))

matches both parities in Definition2.13. The inclusive range0<=k<=d-floor((d+1)/3) and divisor2^(floor(k/2)+1) match Proposition2.15. Theorem1.1 plus Corollary2.10 transfers that necessity to every characteristic-not2 field. Enumerating both(a,b) orientations is valid. Padding/restricting to[2a+1,2b+1,2m] is valid.

### Independent numerical verification

Created `reviewer scratch relation-matrix checker`, without reading or using the scout's matrix code. It implements the full triangular integer relation matrix in Theorem2.7, tests lattice membership through exact integer elimination, reproduces Example2.9's4x4 matrix and Example2.12's obstruction, and checks every witness emitted by `scripts/build.py:bp_obstructions`.

Result: **686/686 emitted BP certificates pass**, including range checks, independent parity-specific binomial evaluation, nondivisibility, and nonmembership in the full relation lattice. No floating point is used.

## Provenance qualification

Precise BP locators refer to the inspected author-final manuscript. Do not label them as theorem wording from arXivv1: that version has a different target convention. Antoniano–Gitler is a direct public theorem plus explicit field-transfer derivation, not an unpublished new mathematical claim.
