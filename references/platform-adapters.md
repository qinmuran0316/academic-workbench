# Platform adapters

The core behavior is host-independent. Before promising a file or a check, inspect the host's actual capabilities. When the user asks to install or configure this Skill, use [AI安装指南.md](../AI安装指南.md) for per-platform prompts and official sources. An ordinary assignment request does not authorize installing tools or changing global settings.

## Codex

Use `SKILL.md` discovery and local workspace tools when available. Keep generated deliverables in the user-requested folder and use the host's document/PDF/terminal tools for verification. Do not assume every Codex session has the same connectors or desktop applications.

## Claude Code

Use the host's supported `SKILL.md` convention: personal `~/.claude/skills/academic-workbench/` or project `.claude/skills/academic-workbench/` when that is the requested scope. Retain the supporting resources and check discovery. Treat browser, PDF, Office, CAD, and network access as conditional; record unavailable checks. Local Claude Code installation does not establish availability in account-backed Claude/Cowork/cloud sessions.

## Claude web, desktop, and Cowork

Use the account's actual custom-skill upload and enablement features when available. Prepare a ZIP containing the complete skill folder. If UI actions cannot be performed, deliver the ZIP and the remaining upload steps; do not claim the account skill was installed or enabled. Cowork account skills and local directories are separate checks.

## WorkBuddy

Use the custom local skill-package upload flow. Its documented conversational search/install flow covers marketplace entries, so do not assume it imports this arbitrary repository URL. Check the installed list and enabled state after an actual import. If only package preparation is possible, report the remaining user action.

## Cursor, Windsurf/Cascade, Copilot, and Gemini CLI

Discover the current client's supported skill locations or installer. Scope installation to the user's requested account/project. Cursor supports `.cursor/skills/`; Copilot in VS Code supports project `.github/skills/`; Gemini CLI has `gemini skills install`. Windsurf/Cascade paths vary with version. Keep the full skill resources, and verify discovery rather than treating file copying as sufficient. Local files do not establish cloud-agent access.

## ChatGPT, Gemini/Gems, 豆包, DeepSeek, Kimi, and Qwen

Inspect the actual surface: native Skill, ZIP import, custom assistant/project instructions, or current-conversation text. Use native support only when it is available in that version. Otherwise provide [通用对话指令.md](../通用对话指令.md), plus relevant materials. If an instruction field is too short, retain full rules as a readable file and provide a short entry instruction. Distinguish temporary use from saved configuration and future memory.

If a repository cannot be accessed, ask for the user-provided files or pasted instruction text; never infer that a private repository is readable because a link was supplied. Request actual artifacts and verification records when the host can produce them; otherwise give reproducible steps marked unperformed.

## Ordinary chat or another AI tool

Use the standalone prompt, provide the task brief and materials, and request the delivery manifest. For source files, request code/text plus exact generation and validation commands. For binary outputs, use a host that can actually write and inspect them. Do not assume a Codex-specific installer or invocation syntax exists in another product.

## Compatibility statement

Compatibility means the instruction set is portable and the workflow degrades honestly. It does not mean every platform can create DOCX, PPTX, XLSX, PDF, DWG, run Java, browse the web, or remember preferences. Report the actual host, tools, versions, and checks.
