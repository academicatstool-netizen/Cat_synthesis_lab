# Verification log

Real captured output of `python examples/verify_dois.py`. Anyone can reproduce
it: clone the repo and run that one command (standard library only, no pip).

It confirms two things at once — that all three papers in the demo are **real,
registered works**, and that the claim the whole demo rests on holds against live
registry data: **Karpicke & Roediger (2008) is about *retrieval*, not *spacing*** —
which is precisely why a disciplined tool must not cite it for a spacing finding.

```text
Verifying 3 example DOIs against the Crossref registry ...

PASS 10.1037/0033-2909.132.3.354  registered: Cepeda 2006, Psychological Bulletin
     “Distributed practice in verbal recall tasks: A review and quantitative synthesis.”
     role in demo: Cepeda et al. 2006, Psychological Bulletin (the genuine spacing meta-analysis)
PASS 10.1126/science.1152408  registered: Karpicke 2008, Science
     “The Critical Importance of Retrieval for Learning”
     role in demo: Karpicke & Roediger 2008, Science (retrieval practice — the trap paper)
PASS 10.1002/acp.1537  registered: Kornell 2009, Applied Cognitive Psychology
     “Optimising learning using flashcards: Spacing is more effective than cramming”
     role in demo: Kornell 2009, Applied Cognitive Psychology (flashcards: spacing beats cramming)

Linchpin claim — Karpicke & Roediger (2008) is about RETRIEVAL, not SPACING:
  PASS — registered title contains "retrieval" and not "spacing".
  So citing it for a *spacing* finding would be a miscredit — exactly what the demo shows the skill avoids.

All three papers are real, and the retrieval-not-spacing claim holds. The demo is grounded in fact.
```

Exit code: `0` (non-zero if any check fails — so this doubles as a CI guard).

Note the registered titles match the demo exactly: Karpicke & Roediger (2008) is
titled *"The Critical Importance of **Retrieval** for Learning"* — there is no
"spacing" in it. That is the factual basis for the example treating it as the
"trap" paper: a spacing-themed review *wants* to cite it for spacing, but its
finding is about retrieval, so crediting it with a spacing result would be a
miscredit. The skill cites it only for the retrieval mechanism.
