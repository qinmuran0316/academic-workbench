# 常见 AI 工具安装与配置

本指南提供可直接发给 AI 的指令。技能名称为 `academic-workbench`，仓库为 `https://github.com/qinmuran0316/academic-workbench`，根目录包含 `SKILL.md`。以下说明按 2026-10-25 查阅的官方文档整理，尚未在这些平台逐一实机安装。

原生技能使用完整目录，至少保留 `SKILL.md`、`references/`、`scripts/` 和 `agents/`。普通对话使用 [通用对话指令.md](通用对话指令.md)。安装器参数和目录以当前工具版本为准，不能将 Codex 的 `$skill-installer` 指令用于所有平台。

仓库为私有时，需要当前环境具备 GitHub 访问权限。无法读取链接时，由有权限的用户下载源码或技能包，再上传给 AI；浏览器已登录不代表 AI 的下载环境也已登录。已有同名技能时，先比较当前版本，按用户授权决定是否更新。

## 通用指令

```text
请从 https://github.com/qinmuran0316/academic-workbench 获取这个作业与论文 Skill，配置到我当前使用的 AI 工具。先确认当前版本与可用工具：能原生加载 Skill 就安装完整目录；需要界面上传就准备技能包和操作步骤；只有对话能力就读取“通用对话指令.md”。无法访问链接时说明需要我提供的文件。最后报告实际安装位置、导入状态或当前对话生效范围，并给出调用示例。
```

<a id="codex"></a>
## Codex

Codex 提供 `$skill-installer`，可以请求它从其他 GitHub 仓库下载技能。[官方文档](https://learn.chatgpt.com/docs/build-skills)

```text
请使用 $skill-installer，从 https://github.com/qinmuran0316/academic-workbench 安装这个 Skill 到我的 Codex。仓库内路径为 .，安装名称为 academic-workbench，请安装完整目录并检查 SKILL.md 和相关参考文件是否可读取。
```

安装器需要参数时使用 `--repo qinmuran0316/academic-workbench --path . --name academic-workbench`。调用示例：`$academic-workbench 按附件题目完成作业`。

<a id="claude-code"></a>
## Claude Code

个人技能可放在 `~/.claude/skills/academic-workbench/`；项目技能可放在项目的 `.claude/skills/academic-workbench/`。下面的指令选择个人安装。[官方文档](https://code.claude.com/docs/en/skills)

```text
请从 https://github.com/qinmuran0316/academic-workbench 下载这个 Skill，安装到我的 Claude Code 个人技能目录 ~/.claude/skills/academic-workbench。仓库根目录就是 Skill，请保留 SKILL.md、references、scripts 和 agents，完成后核对文件和 /academic-workbench 的可用情况。无法访问仓库时请说明需要我提供的文件。
```

调用示例：`/academic-workbench 按附件要求完成课程设计`。Claude Code 本机目录安装与 Claude 账号的云端技能分别管理；本机文件存在不能证明 Cowork 或云端会话已启用。

<a id="claude"></a>
## Claude 网页版、桌面版与 Cowork

Claude 支持上传包含技能文件夹的 ZIP；官方文档中的入口为 `Customize > Skills`，通过创建/上传技能添加，实际可见入口及权限以账号为准。Cowork 使用账号已启用的技能。[上传说明](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [账号与本机技能区别](https://code.claude.com/docs/en/skills)

```text
请读取 https://github.com/qinmuran0316/academic-workbench，帮我准备可上传到 Claude 的 academic-workbench 技能 ZIP。ZIP 中保留完整技能文件夹，说明当前 Customize > Skills 中的上传和启用步骤。若当前工具能操作界面，请完成后核对技能列表；否则交付文件并明确还需我执行的操作。读取不了私有仓库时，我可以上传源码。
```

安装成功后可直接请求：“使用 Academic Workbench，按附件完成课程论文”。以技能列表的导入和启用状态为准。

<a id="workbuddy"></a>
## WorkBuddy

WorkBuddy 支持在技能板块通过“添加技能 > 上传技能”导入自定义本地技能包。官方文档将对话查找安装限定为技能市场中的技能，本仓库采用自定义技能包上传方式。[官方文档](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)

```text
请从 https://github.com/qinmuran0316/academic-workbench 获取这个 Skill，帮我配置到 WorkBuddy。请准备完整的本地技能包，按“技能 > 添加技能 > 上传技能”导入。若当前没有界面操作能力，请交付技能包和操作步骤；导入后再核对已安装列表和启用状态。无法访问仓库时请告诉我需要上传的文件。
```

准备好 ZIP 后仍需完成导入。调用示例：“使用 academic-workbench 完成这份作业，并提供检查记录”。

<a id="doubao"></a>
## 豆包

豆包官方介绍包含智能体定制，但该页面未建立直接导入本仓库 `SKILL.md` 的能力。本指南使用通用对话版；若当前入口提供智能体配置，可由用户把指令填入相应配置。[官方介绍](https://www.doubao.com/legal/feature_intro)

```text
请读取 https://github.com/qinmuran0316/academic-workbench 中的“通用对话指令.md”，按其中规则帮助我完成作业和论文。若链接无法读取，请让我粘贴内容或上传文件。若当前豆包入口提供可编辑的智能体指令，请给出适合填入的配置内容；否则在本对话中使用，并说明实际生效范围。
```

能够读取或遵循指令不等于已经安装本地技能，也不证明具备 Python、Java、CAD 或 Office 文件执行能力。

<a id="cursor"></a>
## Cursor

Cursor 支持本地技能目录，例如个人目录 `~/.cursor/skills/academic-workbench/` 或项目目录 `.cursor/skills/academic-workbench/`。此仓库采用文件夹安装方式；本仓库没有 Cursor 插件市场清单。[官方文档](https://cursor.com/docs/skills)

```text
请从 https://github.com/qinmuran0316/academic-workbench 下载完整 Skill，安装到 Cursor 当前使用的个人技能目录，优先检查 ~/.cursor/skills/academic-workbench。保留全部技能资源，完成后检查技能发现结果，并说明如何通过 /academic-workbench 或当前界面的技能菜单调用。
```

本地技能的安装状态与云端 Agent 的可用状态分别核对，不能由本机文件推断已经云端同步。

<a id="windsurf"></a>
## Windsurf / Cascade

官方原 Windsurf 技能页面当前重定向到 Devin Desktop/Cascade 文档，技能目录随版本变化。让当前客户端确认实际目录，比统一写死路径更合适。[官方文档入口](https://docs.windsurf.com/windsurf/cascade/skills)

```text
请从 https://github.com/qinmuran0316/academic-workbench 下载这个 Skill，配置到我当前使用的 Windsurf/Cascade。先检查客户端版本和其官方支持的 Skills 目录或导入入口，再安装完整的 academic-workbench 文件夹。完成后核对技能是否可发现，并告诉我实际安装位置与调用方式。
```

<a id="copilot"></a>
## GitHub Copilot（VS Code）

VS Code 的 Copilot 支持项目目录 `.github/skills/academic-workbench/`。下面的指令仅配置当前项目。[官方文档](https://code.visualstudio.com/docs/agent-customization/agent-skills)

```text
请从 https://github.com/qinmuran0316/academic-workbench 下载完整 Skill，放到我当前 VS Code 项目的 .github/skills/academic-workbench/。先确认当前使用的是支持 Agent Skills 的 Copilot 环境，保留全部参考与脚本，完成后核对技能列表，并说明如何调用 /academic-workbench。
```

<a id="gemini-cli"></a>
## Gemini CLI

Gemini CLI 提供 `gemini skills install`，可从 Git 仓库或本地目录安装。[官方文档](https://geminicli.com/docs/cli/skills/)

```text
请从 https://github.com/qinmuran0316/academic-workbench 安装这个 Skill 到我的 Gemini CLI。先核对当前版本 gemini skills install 的参数和安装范围；仓库根目录就是 academic-workbench 技能。使用现有 GitHub 访问权限，安装后通过技能列表确认实际加载结果，并告诉我如何使用。
```

若当前版本不能从仓库根目录直接发现技能，先下载完整文件夹，再使用该版本支持的本地安装方式。

<a id="gemini"></a>
## Gemini / Gems

Gemini 网页版的 Gems 可以配置指令并补充文件材料；这与 Gemini CLI 的本地技能安装分别处理。[官方文档](https://support.google.com/gemini/answer/15235603)

```text
请读取 https://github.com/qinmuran0316/academic-workbench 中的“通用对话指令.md”，帮我准备一个名为 Academic Workbench 的 Gemini Gem。提供可填入的指令和需要添加的材料，并说明保存步骤。若当前不能创建或保存 Gem，请在本对话中先遵循这些规则，明确哪些配置还需要我完成。
```

<a id="chatgpt"></a>
## ChatGPT

ChatGPT 的 Skill、插件与本地文件能力按实际入口确认，普通聊天还可使用指令文件或可用的自定义指令设置。本仓库是独立 Skill，尚未封装为各市场的插件。[技能文档](https://learn.chatgpt.com/docs/skills-and-plugins) · [自定义指令](https://learn.chatgpt.com/docs/personalize)

```text
请读取 https://github.com/qinmuran0316/academic-workbench，帮我在当前 ChatGPT 中使用这个作业与论文工作台。先确认当前入口是否能导入独立 Skill；能导入时使用完整目录，若需插件封装请说明实际缺少的步骤。普通聊天则读取“通用对话指令.md”作为本对话规则。无法读取链接时请让我上传文件，并说明实际生效范围。
```

如果配置框有长度限制，提供短入口并将完整规则作为可读取文件，不要静默截断关键规则。

## 其他常见聊天工具

以下分别提供可复制的通用对话指令，未据此确认这些产品的原生 Skill 导入功能。若当前版本提供技能、项目或自定义助手入口，再按该版本实际能力配置。

<a id="deepseek"></a>
### DeepSeek

```text
请在当前 DeepSeek 对话中读取并遵循 https://github.com/qinmuran0316/academic-workbench 的“通用对话指令.md”，作为我的作业与论文工作规则。若链接无法读取，请让我粘贴内容或上传文件。完成后概括已读取的规则，并说明它们在当前对话中的生效范围。
```

<a id="kimi"></a>
### Kimi

```text
请在当前 Kimi 对话中使用 https://github.com/qinmuran0316/academic-workbench 的“通用对话指令.md”，帮助我完成作业、论文和课程设计。若无法访问链接，请让我提供文件；若当前提供可配置的助手或项目入口，请说明如何保存这些规则，否则在本对话中遵循，并明确实际生效范围。
```

<a id="qwen"></a>
### 通义千问 / Qwen

```text
请在当前通义千问/Qwen 对话中读取 https://github.com/qinmuran0316/academic-workbench 的“通用对话指令.md”，作为作业与论文工作台使用。无法读取仓库时请让我粘贴内容或上传文件。若当前入口支持自定义助手，请给出可填写的指令；实际保存或启用完成后再报告配置成功。
```

## 配置完成后检查什么

- 本地安装：报告真实目录，确认 `SKILL.md` 和关联资源可读取，再确认宿主是否发现技能。
- 技能包导入：确认上传、导入与启用状态；只准备文件时列出还需执行的操作。
- 通用对话版：确认实际读到文件，说明当前对话或已保存助手的范围；不能承诺未具备的跨对话记忆。
- 各平台都按真实工具权限执行联网、文件生成、代码运行和 CAD 检查。安装说明已核对，平台实机安装尚未逐一验证。
