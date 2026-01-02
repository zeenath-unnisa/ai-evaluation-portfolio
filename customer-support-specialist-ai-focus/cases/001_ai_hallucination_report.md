## Case ID
_# AI HALLUCINATION REPORT (Case 001)_

## Customer Message
"The AI-generated summary includes metrics that do not exist in our dataset. This is concerning because it was used in a client presentation."

## Category
AI Output Quality

## Context
B2B AI product — generated insights used for business reporting

## Severity
SEV-2 (High)

## Initial Assessment
- Potential AI hallucination caused by ambiguous input, missing constraints, or insufficient grounding in the selected dataset.
- Elevated risk due to potential impact on business decision-making.
- Initial assessment based on reported behaviour; requires confirmation through prompt and dataset review.

## Clarifying Questions
- Can you share the prompt or input used to generate the summary?
- Which dataset or workspace was selected at the time?
- Has this behaviour occurred more than once?
- Was the output edited or used directly as generated?

## Draft Customer Response
Thank you for flagging this — I understand how concerning it is when AI-generated outputs don’t reflect your actual data.

AI systems can generate plausible-looking information when inputs are ambiguous or insufficiently constrained. I’d like to review the specific prompt and dataset context so we can better understand what caused this behaviour and help prevent it going forward.

## Internal Notes
- Review prompt structure and dataset grounding
- Confirm whether constraints were applied
- Check for similar reports from other customers

## Workaround (If Applicable)
- Apply clearer constraints in prompts
- Validate outputs before external use
- Use recommended best practices for data-bound generation

## Escalation Decision
Yes — escalate due to business risk and potential trust impact.
