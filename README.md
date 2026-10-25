# Academic Workbench

跨学段、跨专业的作业与论文 Skill。默认使用简体中文，适用于初中、高中、本科和研究生的课程作业、论文、实验、工程与软件课程设计。

材料充分时直接完成可供检查修改的成品；只有会改变结果的重大缺口才提问。用户要求自主完成时，记录合理假设并持续推进。

## AI 安装（复制给 Codex）

把下面这段话直接发给 Codex：

```text
请从 https://github.com/qinmuran0316/academic-workbench 下载这个 Skill，安装到我的 Codex。请优先使用 $skill-installer；Skill 位于仓库根目录，安装名称为 academic-workbench。请保留完整的 SKILL.md、references、scripts 和 agents，安装后检查文件完整性，告诉我安装位置和调用方式。
```

如果 AI 需要安装器参数，对应 `--repo qinmuran0316/academic-workbench --path . --name academic-workbench`。安装到当前 Codex 实际使用的技能目录；若已有同名技能，先比较现有版本，按本次授权决定是否更新。

仓库为私有时，安装环境需要已登录有访问权限的 GitHub 账号。安装成功后可这样调用：

```text
$academic-workbench 按附件题目和评分标准完成作业，输出可编辑成果和检查记录。
```

安装和调用机制参见 [Codex 官方技能文档](https://developers.openai.com/codex/skills)。

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
