# Academic Workbench

跨学段、跨专业的作业与论文 Skill。默认使用简体中文，适用于初中、高中、本科和研究生的课程作业、论文、实验、工程与软件课程设计。

材料充分时直接完成可供检查修改的成品；只有会改变结果的重大缺口才提问。用户要求自主完成时，记录合理假设并持续推进。

## AI 安装（常见 AI 工具）

Codex、Claude Code、Claude、WorkBuddy、豆包等均提供对应的可复制指令，完整内容见 [AI 安装指南](AI安装指南.md)。Skill 位于仓库根目录，名称为 `academic-workbench`。仓库为私有时，需要安装环境有 GitHub 访问权限，或由你下载后上传文件。

不知道当前工具适合哪种方式时，可以直接发：

```text
请从 https://github.com/qinmuran0316/academic-workbench 获取这个作业与论文 Skill，并配置到我当前使用的 AI 工具。先检查当前版本的技能导入、文件和执行能力；支持原生 Skill 时安装完整目录，需要上传时准备技能包并说明操作入口，否则读取“通用对话指令.md”作为当前对话规则。无法访问仓库时告诉我需要上传哪个文件。完成后说明配置方式、实际完成的步骤和调用方法。
```

### 按工具选择

| AI 工具 | 配置方式与可复制指令 |
|---|---|
| Codex | [技能安装器](AI安装指南.md#codex) |
| Claude Code | [个人或项目技能目录](AI安装指南.md#claude-code) |
| Claude 网页版 / 桌面版 / Cowork | [自定义 Skill ZIP 上传](AI安装指南.md#claude) |
| WorkBuddy | [准备技能包并上传导入](AI安装指南.md#workbuddy) |
| 豆包 | [通用对话版 / 当前入口支持的智能体配置](AI安装指南.md#doubao) |
| Cursor | [本地技能目录](AI安装指南.md#cursor) |
| Windsurf / Cascade | [当前版本的技能目录](AI安装指南.md#windsurf) |
| GitHub Copilot（VS Code） | [项目技能目录](AI安装指南.md#copilot) |
| Gemini CLI | [CLI 技能安装](AI安装指南.md#gemini-cli) |
| Gemini / Gems | [Gem 指令与材料配置](AI安装指南.md#gemini) |
| ChatGPT | [按当前入口使用 Skill 或通用指令](AI安装指南.md#chatgpt) |
| DeepSeek | [通用对话版](AI安装指南.md#deepseek) |
| Kimi | [通用对话版](AI安装指南.md#kimi) |
| 通义千问 / Qwen | [通用对话版](AI安装指南.md#qwen) |

### Codex

```text
请使用 $skill-installer，从 https://github.com/qinmuran0316/academic-workbench 下载并安装这个 Skill 到我的 Codex。Skill 位于仓库根目录，安装名称为 academic-workbench，请保留完整目录并检查安装结果。
```

### Claude Code

```text
请从 https://github.com/qinmuran0316/academic-workbench 下载这个 Skill，安装到我的 Claude Code 个人技能目录 ~/.claude/skills/academic-workbench。仓库根目录就是 Skill，请保留 SKILL.md、references、scripts 和 agents，完成后检查文件并说明如何使用 /academic-workbench。
```

### Claude 网页版 / 桌面版

```text
请从 https://github.com/qinmuran0316/academic-workbench 获取这个 Skill，帮我准备可上传到 Claude 的技能 ZIP，说明 Customize > Skills 的上传步骤。若当前工具能实际操作上传，请在完成后核对技能列表；只能准备文件时，请明确说明还需我上传。无法访问仓库时，我可以提供文件。
```

### WorkBuddy

```text
请从 https://github.com/qinmuran0316/academic-workbench 获取这个 Skill，帮我配置到 WorkBuddy。请准备完整的本地技能包，按“技能 > 添加技能 > 上传技能”导入；若当前不能操作界面，请把技能包和所需操作交给我。导入后核对已安装列表和启用状态。
```

### 豆包

```text
请读取 https://github.com/qinmuran0316/academic-workbench 中的“通用对话指令.md”，按其中规则帮助我完成作业和论文。若链接无法读取，请让我粘贴内容或上传文件。请根据当前豆包入口支持的能力，提供智能体配置步骤或在当前对话中使用；完成后说明生效范围。
```

其他平台的独立指令、调用示例及官方依据见 [AI 安装指南](AI安装指南.md)。原生安装、上传导入、对话中读取分别记录，实际文件生成和执行能力按当前环境检查。

## 能做什么

| 任务 | 工作内容 |
|---|---|
| 作文与报告 | 作文、读书报告、调研报告、案例分析、翻译和润色 |
| 论文与研究 | 课程论文、文献综述、开题、毕业论文、引用核验、已有稿件修改 |
| 数理与实验 | 推导、统计、数模、数据分析、科学绘图、误差分析、实验报告 |
| 软件课程设计 | Java、Python、C/C++、网页和数据库项目，配套代码、测试、报告和说明 |
| CAD 与工程 | 单位、坐标、图层、尺寸、图纸、预览和几何核查 |
| 文档与答辩 | DOCX、XLSX、PPTX、PDF、Markdown、LaTeX、Typst、HTML、Beamer、讲稿和答辩问答 |
| 学习与批改 | 按评分标准检查、复习计划、模拟题、错题整理、引导辅导和项目续接 |

具体文件生成、联网、程序运行和原生软件操作，取决于 AI 工具实际可用的能力。多学科规则不等于内置全部专业软件，也不等于所有专业都已验收。

## 开始使用

**支持技能目录的工具：** 将整个仓库目录作为 `academic-workbench` 技能目录导入，保留 [SKILL.md](SKILL.md)、`references/`、`scripts/` 和 `agents/`。Codex、Claude Code 等工具按各自的技能配置方式加载；详见 [平台适配](references/platform-adapters.md)。

**普通聊天或自定义助手：** 把 [通用对话指令](通用对话指令.md) 放入助手指令或新对话，再提供题目、材料和模板。WorkBuddy、豆包等工具可在其支持的导入方式与通用对话版之间选择。尚未逐一在各平台安装实测。

示例请求：

> 使用 Academic Workbench，按附件题目和评分标准完成作业。输出可编辑成果、预览和检查记录。优先使用课程材料，缺省信息自行作合理假设，重大缺口才提问。

## 工作原则

- 课程材料与学校模板优先，按需检索并核验外部资料。
- 不编造文献、实验测量、调查结果、程序运行日志或软件验证。
- 代码、图纸、数据、报告和 PPT 使用一致的术语、单位和结论。
- 区分已经生成、结构检查、实际运行与原生软件验证；不能执行的步骤明确标记。
- 根据用户样文改善表达，不承诺 AI 检测分数。

## 可选辅助脚本

核心指令不依赖本地脚本。脚本需要 Python 3.10 或更高版本；DXF 解析还需要同一解释器安装 `ezdxf`。

```text
python scripts/capabilities.py
python scripts/check_delivery.py delivery.json --root .
python scripts/inspect_dxf.py drawing.dxf --require-mm
```

能力探测只读；交付检查器不执行清单中的命令。DXF 解析审计不等于 AutoCAD 原生验证。清单格式见 [交付规范](references/delivery-manifest.md)。

## 验证记录

2026-10-25 的自测包含 32 项辅助脚本测试、10 项真实 Java 进程测试、CAD 几何核查和六类行为场景。测试材料、日志及临时依赖已按用户要求删除，本仓库保留 Skill 与历史结果摘要。没有进行原生 AutoCAD 验证或所有 AI 平台的端到端导入测试。

详细使用方式及边界见 [使用与测试说明](使用与测试说明.md)。
