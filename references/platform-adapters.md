# Platform adapters

The core behavior is host-independent. Before promising a file or a check, inspect the host's actual capabilities.

## Codex

Use `SKILL.md` discovery and local workspace tools when available. Keep generated deliverables in the user-requested folder and use the host's document/PDF/terminal tools for verification. Do not assume every Codex session has the same connectors or desktop applications.

## Claude Code

Place the skill in the configured skills directory using the host's supported `SKILL.md` convention. Use shell tools for scripts and repository files. Treat browser, PDF, Office, CAD, and network access as conditional; record unavailable checks.

## WorkBuddy and 豆包

Use the platform's supported skill/agent instruction import when available, or paste [通用对话指令.md](../通用对话指令.md). Upload the relevant reference files or templates. Ask the platform to return artifacts and verification logs; if it cannot run code or inspect files, give reproducible commands for a local environment and mark the check unperformed. Do not claim native integration from a pasted prompt.

## Ordinary chat or another AI tool

Use the standalone prompt, provide the task brief and materials, and request the delivery manifest. For source files, request code/text plus exact generation and validation commands. For binary outputs, use a host that can actually write and inspect them.

## Compatibility statement

Compatibility means the instruction set is portable and the workflow degrades honestly. It does not mean every platform can create DOCX, PPTX, XLSX, PDF, DWG, run Java, browse the web, or remember preferences. Report the actual host, tools, versions, and checks.
