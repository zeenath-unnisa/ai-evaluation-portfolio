## Case ID
_# AI HALLUCINATION REPORT (Case 001)_

## Customer Message
"The AI-generated summary includes metrics that do not exist in our dataset.
This is concerning because it was used in a client presentation."

## Initial Assessment
Potential AI hallucination impacting business decision-making.

## Clarifying Questions
- Can you share the input prompt used?
- Which dataset or workspace was selected?
- Was the output edited before use?

## Category
AI Output Quality

## Severity
SEV-2 (High)

## Draft Customer Response
Thank you for flagging this — I understand how concerning it is when generated outputs don’t reflect your actual data.

Our AI generates summaries based on patterns it detects in the selected dataset, but it does not independently verify metrics unless explicitly constrained. I’d like to gather a few details so we can reproduce and investigate this properly.

## Internal Notes (Engineering)
- Possible hallucination when prompt lacks metric constraints
- Check dataset context window
- Review model confidence thresholds

## Escalation Decision
Escalate to AI/ML team due to risk of incorrect business reporting.
