# Independent review and parent adjudication

Date: 2026-09-26. **Accepted after review.** These are separate AI-agent reviews, not external human peer review.

## Coverage

| Required review | Completed |
|---|---|
| At least five exact cells | Seven: (1,1), (2,2), (4,4), (8,8), (9,9), (10,10), (17,18) |
| At least five unequal brackets | Eight: (11,11), (12,12), (13,13), (14,14), (16,16), (18,18), (20,20), (24,24) |
| Most recent construction | Zhang–Zhu v2 array checked independently by two agents; all 20,736 exact coefficient equations passed |
| Classical table transcription | All 28 Smith–Yiu upper entries, 248 Shapiro upper entries, and 64 oriented sigma entries checked |
| Every restriction-dependent accepted bound | All 129 restriction-labeled records: four upper, 27 sigma lower, 98 BP2 lower |
| Direct sums | All 42 recorded direct sums and their full source ancestry checked |
| Complete ledger integrity | Both reviewers checked all 528 rows and all 1,056 derivation records |

Of the 129 restriction-labeled records, 109 strictly reduce source dimensions; the others use the same source dimensions, sometimes in exchanged orientation. Every relevant row is covered, not merely a sample.

## Independent methods

The reviewers wrote arithmetic and graph checks independently of the builder. The retained [independent checker](../scripts/independent_check.py) does not import the builder or main validator. It recomputes the parity, divisibility, source dimensions, output sums, source ancestry, exact flags, and acyclicity. A separate reviewer also checked all 686 candidate BP2 certificates against the full integer relation matrix in Dugger–Isaksen Theorem 2.7. The maximal retained dependency depth is five.

The parent read the relevant primary source statements, reviewed the field transfers and table pages, reran the construction verifier and independent checker, and accepted the supported bounds. No numerical discrepancy remained. The parent retained the access/version qualifications rather than interpreting a passed arithmetic check as an exhaustive literature audit.

## Detailed reports

- [Primary-source and row review](reviews/frontier.md)
- [Complete derivation review](reviews/derivations.md)
- [Independent lower-theorem review](reviews/lower-theorems.md)

Each report records the reviewed snapshot hashes and limitations. The source-table, CSV, and derivation fingerprints agree across reviewers. Editorial changes to documentation after review do not change these numerical artifacts. [Known gaps](KNOWN_GAPS.md) are part of the acceptance decision.

## Clean-room check

All numerical source leaves resolve to public records. The parent and delegated auditors used public sources, and the new repository began as an empty directory. Private lab values, proof content, amendments, branches, and status labels were not copied or used as authority. The data does not claim private exact closures for sizes 11 or 12.
