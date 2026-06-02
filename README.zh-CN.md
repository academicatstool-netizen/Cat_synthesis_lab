<div align="center">

[English](README.md) · **中文**

<img src="assets/cover-zh.png" alt="AcademiCats · Synthesis Lab" width="100%">

<br>

# 🐱 文献写作台

**把你的文献变成专业的学术写作 —— 综述、研究计划、文书、申请文书、简历。每条引用都追溯到真实论文，并在你看到之前就完成核验。**

<br>

[![License: MIT](https://img.shields.io/badge/License-MIT-7C5CFF.svg)](LICENSE)
&nbsp;[![Runs on Claude](https://img.shields.io/badge/运行于-Claude-7C5CFF.svg)](https://claude.com/claude-code)
&nbsp;[![Full product](https://img.shields.io/badge/完整产品-academicats.com-7C5CFF.svg)](https://academicats.com)

</div>

---

> ### 🪶 这是 [**AcademiCats**](https://academicats.com) 的**开源轻量版**
> 完整产品在 **[academicats.com](https://academicats.com)** —— 一个 AI 研究工作台，带你从*找文献*一路走到*读、写、自审*：拥有项目保存、实时引用工具、精致编辑器和多智能体审稿。本 skill 是其中写作工作流的一块免费、自包含、可在你自己的 Claude 上运行的切片。

---

## ✨ 它能做什么

✍️ **凭*你的*文献写作** —— 给它几篇论文和你的核心论点，它会规划、起草、评审、润色，产出一篇连贯成稿，覆盖**十种文体**，从文献综述到博士申请文书再到简历。

🔗 **可信赖的引用** —— 它**只**引用你提供的论文，**只**在原文出现时才使用具体数字或引文，并在交付前**逐条核验**每个文内引用是否对得上你的文献池。绝不杜撰作者、年份或发现。

🧭 **它会甄选，不只是写** —— 真正不契合你论点的论文会被**附理由搁置**，而不是为了显得详尽硬塞进去。

<br>

## 🎬 演示

> *"用这三篇论文，帮我写一篇短文献综述，论点是间隔重复能提升长期记忆。"* —— 然后粘贴 Cepeda et al. (2006)、Karpicke & Roediger (2008)、Kornell (2009)。

它会先弹一个**写作设置**让你选——主动权在你手上，换任何大模型都一样：

> ✍️ **写作设置** —— 确认或修改，然后我就开写：
> 1. **文体** —— 文献综述
> 2. **核心论点** —— 间隔重复能提升长期记忆
> 3. **引用格式** —— APA 7th
> 4. **篇幅** —— 约 250 词
> 5. **语言** —— 英文
>
> 回复任何修改，或直接说 **go**。

确认后，它返回的成品**永远是同一种结构**——正文、参考文献、一段诚实页脚——换任何大模型跑都一样：

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
> ✅ **引用已核验** —— 每个文内引用都对得上你提供的论文（引用了 3 篇 · APA 7th）。未做改动。
> 📄 **文献综述** · 用了 3 篇中的 3 篇 · 约 250 词

🔎 **它通过的诚实测试：** Karpicke & Roediger 讲的是*提取练习*而非*间隔*—— 所以它只被引用来解释提取机制，**绝不冒充成那篇论文的发现**。这种克制正是本 skill 的全部价值所在。

<br>

## 🚀 60 秒上手

```bash
# 安装到 Claude Code 的 skills 目录 —— 无依赖、零配置
mkdir -p ~/.claude/skills
git clone https://github.com/jy1529098645-gif/Cat_synthesis_lab.git ~/.claude/skills/synthesis-lab
```

重启 Claude Code，然后直接跟它说 —— *"用这几篇论文帮我写论点为 X 的文献综述…"* 或 *"把我的经历写成 CS 博士申请文书。"* skill 会**自动触发**，全程跑在你自己的 Claude 上。

<br>

## 💙 它能写的十种文体

文献综述 · 理论框架 · 研究计划 · 引言 · 讨论 · 结论 · 摘要 · 学术论说文 · **个人陈述 / 申请文书（SoP）** · **简历 / CV**

|  | 文献写作台（本 skill） | [AcademiCats 完整产品 →](https://academicats.com) |
|---|:---:|:---:|
| 有据写作、引用核验 | ✅ | ✅ |
| 内置文献检索与精读 | 自备文献 | ✅ 端到端 |
| 项目保存与实时引用管理 | — | ✅ |
| 对草稿的多智能体同行评审 | — | ✅ Paper Review |

## 🐱 AcademiCats 技能家族

三个开源 skill，串起一条完整的研究工作流——按需安装其一或全部：

- 🔍 [论文检索](https://github.com/jy1529098645-gif/Cat_paper_search) —— 找文献、读文献
- ✍️ **文献写作台** *（你在这里）* —— 据你的文献写出有据成稿
- 🧪 [模拟同行评审](https://github.com/jy1529098645-gif/Cat_paper_review) —— 对你自己的草稿做同行评审

**一次装齐三个** —— clone 任意一个仓库后运行 `bash install.sh`。

## 🙋 常见问题

- **没触发？** 安装后重启 Claude Code，并把话说成一个任务 —— *"用这几篇论文帮我写文献综述…"*。
- **论文从哪来？** 你自己粘进来——或者搭配 **论文检索** 先找好、读好，再据结果写作。
- **用哪个模型？** 任何模型都能跑；用 Claude Sonnet 及以上效果最好。
- **隐私 & 免费？** 全程跑在你自己的 Claude 上——无需账号、不向我们回传任何东西。

<div align="center">
<br>

### 想要完整的研究工作流？
**→ [academicats.com](https://academicats.com) ←**

<br>

由 [AcademiCats](https://academicats.com) 团队用 💙 打造 · [MIT 许可证](LICENSE)

</div>
