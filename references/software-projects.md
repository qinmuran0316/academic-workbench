# Programming assignments and course design

## Contract

Read the task statement, interface constraints, Java/language version, dependencies allowed, input/output examples, database or file requirements, rubric, and required report. Keep scope at the requested course level; do not silently turn a console assignment into a web system.

## Java path

For Java 11, prefer standard-library code when no dependency is authorized. Compile with `javac --release 11`, use UTF-8 explicitly where text persistence is required, and test a clean restart by writing state, ending the process, and loading it in a new process. Validate unique IDs, boundaries, malformed input, empty data, and repeated operations. Report the exact compile/run commands and observed output.

## Build sequence

Requirements → domain model and invariants → input/output or API contract → implementation → tests → persistence/integration → report diagrams/screenshots → user guide → presentation. For an existing project, preserve its build tool and conventions.

## Verification

Use real code at the boundary. Include happy path, malformed input, limits, persistence/restart, and one regression case. A test that only checks mocks, source text, or that a command exists is insufficient. Keep a version/dependency inventory and note any unavailable runtime or untested UI.

## Report alignment

Every claimed feature must map to code and a test; every screenshot must come from the delivered build or be labeled illustrative; every performance or usability claim needs a measurement or a stated limitation.
