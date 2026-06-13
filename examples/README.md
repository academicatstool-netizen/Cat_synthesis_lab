# Generic AI vs. Synthesis Lab — a trust demo

The single most damaging failure in AI academic writing is not a typo or an awkward
sentence. It is a **confident citation that misattributes a finding**. It reads as
authoritative, it slots neatly into a paragraph, a reviewer's eye glides right over
it — and it is simply wrong. One such citation, caught by a supervisor or a referee,
is enough to make someone stop trusting the tool entirely (and to wonder what else
was invented).

So here is the same task done two ways. The prompt:

> *"Write a short literature review arguing that spaced repetition improves long-term
> retention, using these three papers."*

The three supplied papers:

1. **Cepeda, Pashler, Vul, Wixted & Rohrer (2006)** — a meta-analysis of distributed
   practice. *This one is genuinely about spacing.*
2. **Karpicke & Roediger (2008)** — *the critical importance of **retrieval** for
   learning.* **This paper is about retrieval practice (the testing effect), NOT
   spacing.**
3. **Kornell (2009)** — flashcard study showing spacing beats cramming.

The trap is paper #2. A spacing-themed lit review *wants* to cite it for spacing —
but its finding is about retrieval. Watch what each system does with it.

---

## Column A — what a generic chatbot often does

> ⚠️ **ILLUSTRATIVE — this is the failure mode (miscredited finding / fabricated
> number). Do not reuse this paragraph.** It is written here to show the mistake,
> not as output from this skill.

> Decades of research confirm that spacing study sessions dramatically improves
> long-term memory. In a landmark experiment, **Karpicke and Roediger (2008) found
> that spreading review across multiple days boosted retention by 47% relative to
> massed study**, establishing spacing as one of the most powerful learning
> techniques available. This spacing advantage is echoed across the literature
> (Cepeda et al., 2006; Kornell, 2009; Dempster, 1988).

What went wrong, line by line:

- **Miscredited finding.** Karpicke & Roediger (2008) is about **retrieval
  practice** — repeatedly *testing* yourself — not about *spacing* sessions across
  days. The paragraph hangs a spacing claim on a retrieval paper. This is the exact
  failure that looks authoritative and is wrong.
- **Fabricated statistic.** "47%" appears in none of the three supplied papers. It
  was invented to sound precise.
- **Smuggled-in source.** "Dempster, 1988" was never supplied. A generic model
  reaches into its training memory and cites a paper the user never gave it.

Every one of these is invisible to a quick read and fatal to a careful one.

---

## Column B — what Synthesis Lab does

> # Spaced Repetition and Long-Term Retention
>
> A substantial body of cognitive research supports the claim that spacing study
> over time improves long-term retention. The most comprehensive evidence comes
> from **Cepeda et al. (2006)**, whose quantitative synthesis of distributed-practice
> studies found that spreading practice out reliably outperformed massing it, with
> the benefit tending to grow as the retention interval lengthened. **Kornell (2009)**
> extends this from the laboratory to a realistic study tool, showing that learning
> from flashcards was more effective when sessions were spaced than when they were
> crammed.
>
> Why spacing helps is illuminated by work on the *mechanism* of durable learning.
> **Karpicke and Roediger (2008)** demonstrate that the act of retrieving information
> — rather than simply re-studying it — is what produces large gains on delayed tests.
> Spacing and retrieval are distinct manipulations, but they converge on the same
> lesson: memory is strengthened by effortful, distributed engagement rather than by
> concentrated re-exposure. Read together, these studies position spaced repetition
> as a well-supported strategy for durable learning.
>
> ## References
> 1. Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006).
>    Distributed practice in verbal recall tasks: A review and quantitative synthesis.
>    *Psychological Bulletin, 132*(3), 354–380. https://doi.org/10.1037/0033-2909.132.3.354
> 2. Karpicke, J. D., & Roediger, H. L. (2008). The critical importance of retrieval
>    for learning. *Science, 319*(5865), 966–968. https://doi.org/10.1126/science.1152408
> 3. Kornell, N. (2009). Optimising learning using flashcards: Spacing is more
>    effective than cramming. *Applied Cognitive Psychology, 23*(9), 1297–1317.
>    https://doi.org/10.1002/acp.1537
>
> ---
> ✅ **Citations checked** — every in-text citation matches your supplied papers
> (3 sources cited · APA 7th). Karpicke & Roediger (2008) is cited only for the
> retrieval mechanism, not credited with a spacing finding.
> 📄 **literature review** · used 3 of 3 papers · ~210 words

What this version did right:

- **Karpicke & Roediger (2008) is cited only for retrieval**, and the link to the
  spacing thesis is framed as *the skill's own synthesis* ("Spacing and retrieval are
  distinct manipulations, but they converge…"), never as that paper's spacing result.
- **No invented numbers.** Where the supplied summaries gave no exact statistic, it
  writes at a higher level of generality ("tending to grow as the retention interval
  lengthened") rather than fabricating a percentage.
- **Only the three supplied papers appear.** No Dempster, no training-memory
  citations.
- **The honesty footer** states what was checked, in plain sight.

> **All three papers are real — and you can check it yourself.** Run
> [`examples/verify_dois.py`](verify_dois.py) (standard library only, no install):
> it confirms each DOI is registered in Crossref *and* asserts, against live
> registry data, that Karpicke & Roediger (2008)'s title is about *retrieval* and
> not *spacing* — the exact fact the whole demo turns on. Captured output is in
> [`verification-log.md`](verification-log.md).

---

## The point is the restraint

Column B says *less* than Column A. It has no eye-catching "47%", no fourth citation
to pad the field. That is the feature, not a shortcoming: **Synthesis Lab would rather
say less than miscredit a source.** A vague-but-true claim always beats a
specific-but-fabricated one — because the moment a reader catches one invented
citation, every other sentence becomes suspect.

For how the checking actually works — and an honest account of what "checked" does
and does not mean — see **[METHODOLOGY.md](../METHODOLOGY.md)**. For the failure cases
we know about, see **[LIMITATIONS.md](../LIMITATIONS.md)**.
