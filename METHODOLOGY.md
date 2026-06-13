# How citation discipline works

Synthesis Lab's promise is narrow and concrete: it cites **only the papers you
supply**, it uses a **specific number or quote only when that number or quote is in
the source**, and it **cross-checks every in-text citation against your pool before
delivering**. This page explains the rules in plain language — and, just as
importantly, is honest about what the check *is not*.

## The rules

**1. Cite only supplied papers.**
The model is given your papers — title, authors, year, and an abstract or summary for
each (plus full text or a deep-read report when you provide it). Those are the only
sources it is allowed to cite. It will not reach into its training memory to add a
"classic" reference you didn't give it. If a relevant paper exists in the world but
isn't in your pool, it stays out.

**2. A specific number or quote only if it's in the source.**
Statistics, sample sizes, effect sizes, p-values, dates, and direct quotations are
included **only when they appear verbatim in the material you supplied**. When the
summary is thin, the skill deliberately writes at a higher level of generality
("the advantage tended to grow with longer retention intervals") rather than
inventing a precise figure. A vague-but-true claim always beats a
specific-but-fabricated one.

**3. Cite a paper only for what it actually found.**
A paper earns a citation only for claims its own summary supports. If a paper explains
a *mechanism* that is adjacent to your thesis but doesn't directly demonstrate it
(the classic case: a **retrieval-practice** paper in a **spacing** review), the skill
keeps it but cites it *only* for what it states, and frames the connection to your
thesis as **the skill's own synthesis** — never as that paper's finding. Misattributing
a finding is the exact failure this discipline exists to prevent.

**4. Set aside papers that don't fit — with a reason.**
Not every paper you attach will earn a place. Rather than shoehorning a weak fit in to
look thorough, the skill rejects it and tells you why. A rejected paper appears in no
section and in no bibliography.

**5. Cross-check author/year against the pool before delivery.**
Before handing back a citing document, the skill extracts every in-text citation
(`(Smith, 2021)`, `(Smith et al., 2021)`, `[3]`, `[4–7]`) and matches each one back to
a supplied paper by first-author surname (allowing a one-year drift for in-press
work). It flags and fixes citations whose author isn't in the pool, numbered
references that point past the end of your list, and surnames that match more than one
paper. If it had to soften or remove a claim to make the document pass, it tells you
what changed.

## What "checked" means — and what it doesn't

This is the part most tools quietly skip. Read it.

**"Checked" here is a SOFT, author/year self-consistency check performed by the model
itself.** It confirms that every name and year in the text corresponds to a paper you
actually supplied, that no numbered reference dangles past your list, and that the
specificity and grounding rules above were applied during drafting. That is genuinely
useful: it catches the most common and most damaging failure — a citation pointing at
a paper that was never in your pool, or a finding pinned to the wrong author.

**It is NOT a hard, quote-level verification against the source PDFs.** The skill does
not open your PDFs, locate the exact sentence behind each claim, and confirm
word-for-word that the source supports it. It reasons over the summaries and text you
gave it; it does not re-read the originals to audit itself. So when you see

> ✅ Citations checked — every in-text citation matches your supplied papers

read it as *"the names and years line up with the papers you gave me, and I applied
the grounding rules,"* **not** as *"every sentence has been verified against the source
text."* We say **checked / cross-checked**, never *"verified,"* on purpose.

**Where the hard verification lives.** Quote-level checking — matching each specific
claim to the exact passage in the source PDF — is part of the full product at
**[academicats.com](https://academicats.com)**, which has the live citation tooling
and document context to do it. This open-source skill is the disciplined-drafting
slice; the full product is the audit.

For the concrete boundaries and known failure cases, see **[LIMITATIONS.md](LIMITATIONS.md)**.
