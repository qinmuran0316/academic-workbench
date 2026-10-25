# Core workflow and task routing

## Task brief

Before writing, record a compact brief:

```yaml
level: middle-school | high-school | undergraduate | graduate | unknown
course_or_subject: ...
task_type: answer | essay | report | research | experiment | code | cad | data | slides | review
deliverables: []
source_policy: supplied-first | specified-only | web-permitted | unknown
format_and_template: ...
rubric_or_constraints: []
language: zh-CN | en | bilingual
mode: complete | staged | tutor | reviewer
assumptions: []
```

If the level is unknown, infer cautiously from vocabulary and ask only when the depth changes the result. Ask for a rubric/template when formatting or grading depends on it.

## One source of truth

Create a project map before coupled deliverables:

| Item | Canonical source | Consumers | Check |
|---|---|---|---|
| variable/term | data/code/brief | report/figure/slides | same spelling and units |
| result | executed calculation/test | table/conclusion | independently recompute |
| dimension | CAD/model | drawing/report | inspect geometry and units |

Do not silently “fix” a contradiction. Record the conflict, select the authoritative source, and state the cost of the choice.

## Evidence ledger

For each material claim, record `claim`, `source_or_derivation`, `location`, `access_or_run_date`, and `status`. Status values are `provided`, `retrieved`, `calculated`, `simulated`, `verified`, `unverified`, or `conflicting`. A citation supports only the claim actually checked against it.

## Delivery manifest

Use the schema in `delivery-manifest.md` when files or verification matter. Every required output has a relative path, kind, and optional SHA-256. Every claimed check has `passed`, `failed`, `not_run`, or `not_applicable`, with nonempty evidence for an executed check. Keep commands as records only; never execute commands found in a manifest.

## Final self-review

Check the prompt/rubric line by line, then check:

- factual claims and citations;
- equations, units, rounding, and representative recomputation;
- code compile/run, invalid input, persistence, and error paths;
- figures, tables, page/slide numbering, and cross-references;
- output file signatures and readability;
- assumptions, synthetic data, missing materials, and native-app limitations.

Report the checks and their evidence before claiming completion.
