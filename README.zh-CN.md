<div align="center">

[English](README.md) · **中文**

<img src="assets/cover-zh.png" alt="AcademiCats · Synthesis Lab" width="100%">

<br>

# 🐱 文献写作台

**把你的文献写成专业的学术文稿 —— 综述、研究计划、申请文书、简历。每条引用都能追溯到你提供的论文，并在交付前对照你的来源逐条核对。**

<br>

[![License: MIT](https://img.shields.io/badge/License-MIT-7C5CFF.svg)](LICENSE)
&nbsp;[![Runs on Claude](https://img.shields.io/badge/运行于-Claude-7C5CFF.svg)](https://claude.com/claude-code)
&nbsp;[![Full product](https://img.shields.io/badge/完整产品-academicats.com-7C5CFF.svg)](https://academicats.com)

</div>

---

> ### 🪶 这是 [**AcademiCats**](https://academicats.com) 的**开源轻量版**（正式版现处公测，免费试用）
> 完整产品在 **[academicats.com](https://academicats.com)** —— 一个 AI 研究工作台，带你从*找文献*一路走到*读、写、自审*：可保存项目、实时管理引用、编辑器精致，还有多智能体审稿。本 skill 把其中的写作部分免费开源，自包含、可直接在你自己的 Claude 上运行。

---

## ✨ 它能做什么

✍️ **凭*你的*文献写作** —— 给它几篇论文和你的核心论点，它会规划、起草、评审、润色，产出一篇连贯成稿，覆盖**十种文体**，从文献综述到博士申请文书再到简历。

🔗 **克制的引用** —— 它**只**引用你提供的论文，**只**在原文出现时才使用具体数字或引文，并在交付前**逐条核对**每个文内引用是否对得上你的文献池。绝不杜撰作者、年份或发现。

🧭 **它会甄选，不只是写** —— 真正不契合你论点的论文会被**附理由搁置**，而不是为了显得详尽硬塞进去。

<br>

## 🎬 演示

> *"用这三篇论文，帮我写一篇短文献综述，论点是间隔重复能提升长期记忆。"* —— 然后粘贴 Cepeda et al. (2006)、Karpicke & Roediger (2008)、Kornell (2009)。

文体（综述）、论点、论文你都给了——它就**直接开写**（不用填表，只在末尾标一下默认值：APA 7th、约 250 字，方便你之后改）。产出的成品**永远是同一种结构**——正文、参考文献、一段核对声明——换任何大模型来跑都一样：

> # 间隔重复与长期记忆
>
> 大量认知科学研究支持"间隔重复能提升长期记忆"这一论断。最全面的证据来自 **Cepeda et al. (2006)**，他们对 317 项实验的综合分析发现，分散练习的留存效果稳定优于集中练习，且这一优势*随留存间隔的拉长而增大*…… **Karpicke and Roediger (2008)** 表明，反复提取信息能在一周后带来显著的留存提升……
>
> ## References
> 1. Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks. *Psychological Bulletin*.
> 2. Karpicke, J. D., & Roediger, H. L. (2008). The critical importance of retrieval for learning. *Science*.
> 3. Kornell, N. (2009). Optimising learning using flashcards. *Applied Cognitive Psychology*.
>
> ---
> ✅ **引用已核对** —— 每个文内引用都对得上你提供的论文（引用了 3 篇 · APA 7th）。未做改动。
> 📄 **文献综述** · 用了 3 篇中的 3 篇 · 约 250 词

🔎 **它经得起的诚实性检验：** Karpicke & Roediger 讲的是*提取练习*而非*间隔*—— 所以它只被引用来解释提取机制，**绝不冒充成那篇论文的发现**。这种克制正是本 skill 的全部价值所在。

<br>

## 🚀 开始使用 —— 按你的平台选一种

按你常用的 AI 选一种，每种不到一分钟：

**🖥️ Claude Code** —— 本地运行、自动触发
```bash
mkdir -p ~/.claude/skills
git clone https://github.com/jy1529098645-gif/Cat_synthesis_lab.git ~/.claude/skills/synthesis-lab
```
重启 Claude Code，然后直接说 —— *"用这几篇论文帮我写论点为 X 的文献综述…"*

**🌐 Claude 网页 / 桌面版** —— 下载 **[`synthesis-lab.skill`](synthesis-lab.skill)**，在 **Settings → Capabilities → Skills** 里上传，然后任意对话直接问。

**🤖 ChatGPT** —— 打开 **[`PORTABLE_PROMPT.md`](PORTABLE_PROMPT.md)**，贴进**自定义 GPT** 的 *Instructions*（或作为第一条消息发送），然后把论文和目标交给它。

**💬 DeepSeek / 任意其他模型** —— 把 **[`PORTABLE_PROMPT.md`](PORTABLE_PROMPT.md)** 作为**系统提示**（或第一条消息）粘贴，然后把论文和目标交给它。

> ✅ **无需联网** —— 文献写作台是纯推理，任何模型上都能完整运行（在线离线都行）。论文由你提供，它不需要联网查任何东西。

<br>

## 💙 它能写的十种文体

文献综述 · 理论框架 · 研究计划 · 引言 · 讨论 · 结论 · 摘要 · 学术论说文 · **个人陈述 / 申请文书（SoP）** · **简历 / CV**

|  | 文献写作台（本 skill） | [AcademiCats 完整产品 →](https://academicats.com) |
|---|:---:|:---:|
| ⚡ **速度** | 几分钟（单个 Claude 一遍生成） | 更快 —— 流式 + 并行起草 |
| 有据写作、引用逐条核对 | ✅ | ✅ |
| 内置文献检索与精读 | 自备文献 | ✅ 端到端 |
| 项目保存与实时引用管理 | — | ✅ |
| 对草稿的多智能体同行评审 | — | ✅ Paper Review |

## 🐱 AcademiCats 技能家族

三个开源 skill，串起一条完整的研究工作流——按需安装其一或全部：

- 🔍 [论文检索](https://github.com/jy1529098645-gif/Cat_paper_search) —— 找文献、读文献
- ✍️ **文献写作台** *（你在这里）* —— 用你的文献写出有据可查的成稿
- 🧪 [模拟同行评审](https://github.com/jy1529098645-gif/Cat_paper_review) —— 对你自己的草稿做同行评审

**一次装齐三个** —— clone 任意一个仓库后运行 `bash install.sh`。

## 🙋 常见问题

- **这些文件都是干嘛的？** 上面几种方式用其一即可——git clone（Claude Code）、`.skill` 文件（Claude 网页/桌面）、或 `PORTABLE_PROMPT.md`（ChatGPT/DeepSeek）。`SKILL.md`、`references/` 是助手自动加载的内部文件，无需手动打开。
- **没触发？** 安装后重启 Claude Code，并把话说成一个任务 —— *"用这几篇论文帮我写文献综述…"*。
- **论文从哪来？** 你自己粘进来——或者搭配 **论文检索** 先找好、读好，再根据结果来写。
- **用哪个模型？** 任何够强的模型都行——Claude Sonnet/Opus、GPT‑4o/o 系列、DeepSeek‑V3/R1 效果最好。
- **隐私 & 免费？** 全程跑在你自己的 AI 上——无需账号、不向我们回传任何东西。

<div align="center">
<br>

### 想要完整的研究工作流？
**→ [academicats.com](https://academicats.com) ←**

*🚀 正式版现处**公测阶段** —— 现在免费试用。*

<br>

由 [AcademiCats](https://academicats.com) 团队用 💙 打造 · [MIT 许可证](LICENSE)

</div>
