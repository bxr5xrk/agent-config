# Experiments and measurement

An experiment record should name:

- segment and funnel constraint;
- falsifiable hypothesis and expected mechanism;
- treatment, control/comparison when practical, and exposure unit;
- primary outcome, leading diagnostic metrics, and guardrails;
- instrumentation path from exposure to revenue/retention;
- sample/time/cost cap, invalidation conditions, and next decision.

Prefer the smallest test that can change a decision. Early-stage evidence may be
manual and qualitative, but define what counts before running it. A founder-led
sales pilot can test urgency and willingness to pay; it does not establish
scalable CAC. An A/B test without enough eligible traffic creates false precision.

Verify events at the source and destination. Specify identity, tenant/account,
experiment variant, timestamps, attribution window, and deduplication. Confirm
that the dashboard query matches the product event semantics. Track drop-off and
failure states, not only successful clicks.

Use one primary metric tied to the hypothesis. Guard against channel saturation,
selection bias, novelty effects, seasonality, sales follow-up differences, and
provider outages. Predefine “continue”, “iterate”, and “stop” thresholds; do not
move them after seeing the result without labeling the analysis exploratory.

For irreversible, expensive, reputation-sensitive, or platform-risky tactics,
start with a smaller reversible cohort and an explicit kill switch.
