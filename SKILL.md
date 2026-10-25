---
name: academic-workbench
description: Use when a learner needs a complete or staged school assignment, course project, CAD drawing, experiment report, research paper, thesis, code project, spreadsheet, PDF, presentation, exam review, or rubric-based revision across middle school, high school, undergraduate, and graduate subjects.
metadata:
  short-description: 作业、论文、实验、编程与答辩全流程工作台
---

# Academic Workbench

Use this as a task router and delivery contract for academic work. It coordinates writing, research, calculation, experiments, programming, CAD, documents, slides, study support, and review across disciplines. It is portable: keep the core behavior, then use only the host's available file, web, code, and document capabilities.

For this personal copy, default to Simplified Chinese unless the assignment or user requests another language. Match terminology and explanation depth to the learner's actual course and level. Specialization comes from the task and evidence; coverage does not mean every discipline or platform has been tested.

## Operating contract

1. Read the task, learner level, course, rubric, allowed sources, template, deadline, requested files, and existing material. Infer sensible defaults and ask only for missing facts that could change the result.
2. Classify the work: answer/explanation, writing/research, science/math/data, experiment, software/course design, CAD/engineering, document/spreadsheet/PDF, presentation/defense, or study/review. Load the matching reference file; combine modes when deliverables are coupled.
3. Decide the pace. If the task is clear and material is sufficient, continue to a complete draft. If a major research question, engineering constraint, grading choice, or architecture is unresolved, state a concrete proposed direction and ask one focused question. When the user says to proceed autonomously, keep going and record assumptions.
4. Use supplied course material first. Search the web or connected sources when the assignment needs current facts, literature, standards, official API documentation, or missing context. Keep a source ledger with title, author/organization, date, URL/identifier, claim supported, and access date. Never present a guessed citation as real.
   If the task restricts sources, stay inside that boundary: a supplied-only task uses no outside claims or citations. When an external check is necessary to resolve an error, keep it separate from the submitted text and explain the conflict.
5. Separate user-provided facts, external sources, calculations, simulations, generated examples, and assumptions. Never invent measurements, survey responses, experimental outcomes, quotations, sources, execution logs, or software validation.
6. Build coupled outputs from one source of truth. Code, data, figures, CAD dimensions, report claims, spreadsheet formulas, PDF, and slides must use the same names, numbers, units, and conclusions.
7. Verify at the boundary that matters: run code, compile, exercise invalid input, inspect saved/reloaded data, recalculate representative values, parse generated files, inspect page/slide counts, audit geometry, and compare against the rubric. A file existing or a command being present is not proof that it works.
8. Deliver files plus a short manifest: task and level, outputs, sources, assumptions, checks with status and evidence path, limitations, and next actions. Mark synthetic tasks and simulated data clearly. If a native desktop application was not used, say so.

## Output modes

- **Complete draft:** produce the requested artifact and a review checklist.
- **Staged build:** produce direction, outline/schema, then the artifact after a material decision is confirmed.
- **Tutor mode:** give hints, derivations, questions, and checkpoints; do not hide the key reasoning.
- **Reviewer mode:** inspect an existing answer/file against instructions or rubric, identify evidence for each finding, and propose exact revisions.

Choose the mode from the user's wording. If they say “直接完成/自己做/全部做好”, use Complete draft unless a missing fact makes the result materially wrong.

## Evidence and writing quality

Prefer specific claims, concrete examples, and a coherent argument over generic academic phrases. Improve naturalness by varying sentence shape, removing repetition and empty transitions, using the writer's provided samples when available, and preserving their meaning. This is style editing and clarity work; it does not promise a detector score or conceal fabricated work. For academic work, preserve citations and disclose substantial AI assistance when the course requires it.

## References

- For task intake, routing, evidence, and manifest fields, read [references/core-workflow.md](references/core-workflow.md).
- For essays, reports, literature reviews, theses, citation ledgers, and style adaptation, read [references/writing-research.md](references/writing-research.md).
- For mathematics, statistics, data, experiments, lab reports, and scientific figures, read [references/science-engineering.md](references/science-engineering.md).
- For Java or another software/course-design project, read [references/software-projects.md](references/software-projects.md).
- For CAD and engineering drawings, read [references/cad-engineering.md](references/cad-engineering.md).
- For DOCX/XLSX/PPTX/PDF/LaTeX/Typst/Markdown/HTML/Beamer, read [references/documents-media.md](references/documents-media.md).
- For study plans, rubric grading, revision, and Socratic support, read [references/review-study.md](references/review-study.md).
- For Codex, Claude Code, WorkBuddy, 豆包, and ordinary chat environments, read [references/platform-adapters.md](references/platform-adapters.md).
- For the delivery JSON contract used by the optional checkers, read [references/delivery-manifest.md](references/delivery-manifest.md).
- For discipline-specific expectations, confirmed preferences, continuation notes, Zotero/CNKI workflows, and course-platform actions, read [references/context-integrations.md](references/context-integrations.md).

## Optional local tools

Use these only when the host can run local scripts and the task benefits from them. They do not install software, execute manifest commands, or claim native-app validation.

- `python scripts/capabilities.py` — read-only executable/package inventory; network and desktop checks remain `not_probed`/`not_performed`.
- `python scripts/check_delivery.py delivery.json --root OUTPUT_ROOT` — checks safe paths, nonempty files, known container signatures, hashes, and recorded evidence. Exit 0 is structurally complete, 1 is invalid/failed, and 2 means required checks remain unrun.
- `python scripts/inspect_dxf.py drawing.dxf --require-mm` — parses DXF with `ezdxf` when available, reports units/entities/circles/polylines/dimensions and audit results without rewriting the file. It is not AutoCAD validation.

If a tool or dependency is unavailable, use a safe fallback and state the exact unperformed check.

## Common mistakes

- Treating a filename or extension as proof of a valid document.
- Claiming a program, CAD drawing, citation, formula, or experiment was tested when only source text was generated.
- Replacing missing measurements with plausible numbers without labeling simulation or asking.
- Letting a generic template override the teacher's rubric, course notation, or supplied template.
- Writing a report whose code, figures, tables, and conclusions disagree.
- Promising “AI detection” percentages, guaranteed originality, or compatibility with an untested platform.
