# Mathematics, statistics, data, and experiments

## Computation contract

Write down inputs, units, formula or algorithm, precision, tool/version, and a hand-check or independent check. Keep code and generated data with the result when reproducibility matters. Never round intermediate values unless the method requires it.

For statistics, state the population/sample, variable definitions, missing-data treatment, assumptions, test/model choice, effect size or uncertainty, and what the result does not establish. For numerical work, test boundary cases and dimensional consistency.

## Experimental reporting

Separate four layers:

1. **Given:** instrument records, user data, instructions, or observations.
2. **Derived:** calculations and transformations that can be reproduced.
3. **Simulated/example:** generated values used to demonstrate a method.
4. **Unresolved:** missing calibration, measurement, or environmental facts.

Do not use a plausible replacement for a missing measurement. Ask, or continue with a clearly labeled example and leave the conclusion conditional.

## Figures and tables

Label variables, units, sample size, uncertainty, and source. Use a caption that says what to inspect. Check axis scales, legends, significant figures, and that the text interpretation matches the actual figure. Keep raw data separate from polished tables.

## Math and modeling

State assumptions before deriving. Preserve notation from the course unless a translation is required. Show enough intermediate steps for a learner to audit the result, then provide a compact final answer. For optimization or modeling, test sensitivity to the assumptions and identify infeasible or degenerate cases.
