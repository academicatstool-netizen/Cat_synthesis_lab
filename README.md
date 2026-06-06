<div align="center">

**English** · [中文](README.zh-CN.md)

<img src="assets/cover.png" alt="AcademiCats · Synthesis Lab" width="100%">

<br>

# 🐱 Synthesis Lab

**Turn your sources into polished academic writing — literature reviews, proposals, essays, statements of purpose, résumés. Every citation traces to a paper you supplied, and gets cross-checked against your sources before delivery.**

<br>

[![License: MIT](https://img.shields.io/badge/License-MIT-7C5CFF.svg)](LICENSE)
&nbsp;[![Runs on Claude](https://img.shields.io/badge/runs%20on-Claude-7C5CFF.svg)](https://claude.com/claude-code)
&nbsp;[![Full product](https://img.shields.io/badge/full%20product-academicats.com-7C5CFF.svg)](https://academicats.com)

</div>

---

> ### 🪶 This is the **lite, open-source edition** of [**AcademiCats**](https://academicats.com) — now in free open beta
> The full product at **[academicats.com](https://academicats.com)** is an AI research workbench that takes you from *finding* papers through *reading, writing, and self-review* — with saved projects, live citation tooling, a polished editor, and a multi-agent reviewer. This skill is a free, self-contained slice of the writing workflow you can run on your own Claude.

---

## ✨ What it does

✍️ **Writes from *your* sources** — give it a handful of papers and your core argument; it plans, drafts, reviews, and polishes a coherent piece across **ten document types**, from literature reviews to PhD statements of purpose to résumés.

🔗 **Disciplined citations** — it cites *only* the papers you supply, uses a specific number or quote *only* when it appears in the source, and cross-checks every in-text citation against your pool before delivering. No invented authors, years, or findings.

🧭 **It curates, not just writes** — papers that don't actually fit your thesis get set aside with a reason, instead of being shoehorned in to look thorough.

<br>

## 🎬 Demo

> *"Write a short literature review arguing that spaced repetition improves long-term retention, using these three papers."*  — then paste Cepeda et al. (2006), Karpicke & Roediger (2008), Kornell (2009).

You gave the type (lit review), the thesis, and the papers — so it writes straight away (no forms; it just notes its assumptions — APA 7th, ~250 words — so you can tweak after). What comes back is **always the same shape** — the document, a references list, and an honesty footer — no matter which model runs the skill:

> # Spaced Repetition and Long-Term Retention
>
> A robust body of cognitive research supports the claim that spaced repetition improves long-term retention. The most comprehensive evidence comes from **Cepeda et al. (2006)**, whose synthesis of 317 experiments found distributed practice reliably outperformed massed practice, with the advantage *growing as the retention interval lengthened*… **Karpicke and Roediger (2008)** show that repeatedly retrieving information produces large gains a week later…
>
> ## References
> 1. Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks. *Psychological Bulletin*.
> 2. Karpicke, J. D., & Roediger, H. L. (2008). The critical importance of retrieval for learning. *Science*.
> 3. Kornell, N. (2009). Optimising learning using flashcards. *Applied Cognitive Psychology*.
>
> ---
> ✅ **Citations checked** — every in-text citation matches your supplied papers (3 sources cited · APA 7th). Nothing changed.
> 📄 **literature review** · used 3 of 3 papers · ~250 words

🔎 **The honesty test it passes:** Karpicke & Roediger is about *retrieval*, not *spacing* — so it's cited only for the retrieval mechanism, **never miscredited with a spacing finding.** That discipline is the whole point.

<br>

## 🚀 Get started — pick your platform

Pick whichever AI you use; each setup takes under a minute.

**🖥️ Claude Code** — runs locally, triggers itself
```bash
mkdir -p ~/.claude/skills
git clone https://github.com/jy1529098645-gif/Cat_synthesis_lab.git ~/.claude/skills/synthesis-lab
```
Restart Claude Code, then just ask — *"write the lit review for my thesis arguing X, using these papers …"*

**🌐 Claude (web / desktop app)** — download **[`synthesis-lab.skill`](synthesis-lab.skill)**, then upload it under **Settings → Capabilities → Skills**. Ask in any chat.

**🤖 ChatGPT** — open **[`PORTABLE_PROMPT.md`](PORTABLE_PROMPT.md)** and paste it into a **Custom GPT**'s *Instructions* (or just send it as your first message). Then give it your papers and goal.

**💬 DeepSeek / any other model** — paste **[`PORTABLE_PROMPT.md`](PORTABLE_PROMPT.md)** as the **system prompt** (or first message). Then give it your papers and goal.

> ✅ **No web access needed** — Synthesis Lab is pure reasoning, so it runs fully on any model, online or off. You bring the papers; it never needs to look anything up.

<br>

## 💙 Ten things it can write

Literature review · Theoretical framework · Research proposal · Introduction · Discussion · Conclusion · Abstract · Academic essay · **Personal statement / SoP** · **Résumé / CV**

|  | Synthesis Lab (this skill) | [AcademiCats full product →](https://academicats.com) |
|---|:---:|:---:|
| ⚡ **Speed** | minutes (one Claude pass) | faster — streamed, parallel drafting |
| Grounded writing, citations cross-checked | ✅ | ✅ |
| Built-in paper search & deep read | bring your own | ✅ end-to-end |
| Saved projects & live citation manager | — | ✅ |
| Multi-agent peer review of your draft | — | ✅ Paper Review |

## 🐱 The AcademiCats skill family

Three open skills that chain into one research workflow — install any or all:

- 🔍 [Paper Search](https://github.com/jy1529098645-gif/Cat_paper_search) — find & read papers
- ✍️ **Synthesis Lab** *(you are here)* — write grounded papers from your sources
- 🧪 [Paper Review](https://github.com/jy1529098645-gif/Cat_paper_review) — peer-review your own draft

**Install all three at once** — clone any one repo, then run `bash install.sh`.

## 🙋 FAQ

- **What are all these files?** Use just one path above — a git clone (Claude Code), the `.skill` file (Claude web/desktop), or `PORTABLE_PROMPT.md` (ChatGPT/DeepSeek). `SKILL.md` and `references/` are internals your assistant loads for you — no need to open them.
- **It didn't trigger?** Restart Claude Code after installing, and phrase your message as a task — *"write the lit review from these papers …"*.
- **Where do the papers come from?** You paste them in — or pair this with **Paper Search** to find and read them first, then write from the results.
- **Which model?** Any strong model works — Claude Sonnet/Opus, GPT‑4o/o‑series, or DeepSeek‑V3/R1 give the best results.
- **Private & free?** It runs on your own AI — no account, nothing sent to us.

<div align="center">
<br>

### Want the whole research workflow?
**→ [academicats.com](https://academicats.com) ←**

*🚀 The full product is in **open beta** — free to try right now.*

<br>

Made with 💙 by the [AcademiCats](https://academicats.com) team · [MIT License](LICENSE)

</div>
