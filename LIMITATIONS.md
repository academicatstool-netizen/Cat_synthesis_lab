# Known limitations

Synthesis Lab is built around one discipline — cite only what you supplied, and only
for what it says — and it does that well. But it is a reasoning tool, not an oracle.
Here are the boundaries we know about, written down so you can decide where to trust
it and where to double-check.

## 1. It can only be as good as the papers you supply

Garbage in, garbage out. The skill writes from the titles, authors, years, and
summaries you give it. If a summary is inaccurate, outdated, or itself misstates a
paper's finding, the skill will faithfully build on that error — it has no
independent knowledge of the literature to correct you with. Supply accurate sources,
and prefer fuller text (a deep-read report or the PDF) over a one-line abstract when
the claim matters.

## 2. The cross-check is at the author/year level

The pre-delivery check matches **surnames and years** against your pool (see
[METHODOLOGY.md](METHODOLOGY.md)). It reliably catches a citation pointing at a paper
you never supplied, or a numbered reference past the end of your list. It is **weaker
against a subtly miscredited claim that is phrased vaguely.** If a sentence attributes
a slightly-wrong finding to a paper that *is* in your pool, using hedged language, the
author/year check will see a valid name-and-year and may let it through. The grounding
rules push against this during drafting, but the final safety net is name-level, not
meaning-level — so read claims on borderline papers (e.g. a mechanism paper used in a
review about something adjacent) with your own eyes.

## 3. It does not fetch or verify full text

The skill does not browse, download, or open your PDFs to confirm a quote word-for-word
against the source. "Checked" means *author/year self-consistency*, not *quote-level
verification*. Quote-level checking against source text is what the full product at
[academicats.com](https://academicats.com) is for.

## 4. Bibliographic fields are only as complete as what you give it

The references list is built from the fields present in your paper records. The skill
**will not invent** volume, issue, page ranges, or article numbers to make a reference
look "complete" — a short reference with only author/year/title/journal is correct; a
plausible-looking but fabricated one is not. If you want full APA volume(issue), pp.
entries, supply those fields (or a DOI) with each paper. A reference may therefore come
back deliberately sparse.

## 5. Quality varies by model

This skill is pure reasoning that runs on whatever model you point it at. Stronger
models (Claude Sonnet/Opus, GPT‑4o/o‑series, DeepSeek‑V3/R1) follow the grounding and
cross-check discipline more reliably; weaker or heavily quantised models are more
likely to drift, over-specify, or miss a miscredit. The discipline is instructions, not
a hard runtime guarantee — a more capable model honours it more faithfully.

---

None of these are reasons not to use the skill — they are the honest edges of a tool
whose whole value is *not* overclaiming. When a claim is load-bearing for your work,
verify it against the source yourself, or use the full product's quote-level checking.
