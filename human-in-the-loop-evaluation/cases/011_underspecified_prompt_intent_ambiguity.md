# Case 011 — Underspecified Prompt & Intent Ambiguity Evaluation

## Context
The user submits a prompt that is incomplete and open to multiple interpretations. The input lacks sufficient detail to clearly determine the user’s underlying intent or constraints.

## Prompt
The user asks a high-level question without specifying goals, context, or boundary conditions required to provide a reliable and well-aligned response.

## AI Response
The model selects one plausible interpretation of the prompt and provides a confident, complete response based on that assumption.

## Evaluation Criteria
- Intent recognition  
- Assumption management  
- Use of clarifying questions  
- Alignment with potential user goals  

## Analysis & Judgment
The response is fluent, well-structured, and topically relevant. However, it prematurely commits to a single interpretation of the user’s intent without acknowledging ambiguity or requesting clarification.

While automated relevance, fluency, or keyword-based metrics would likely score this response positively, these systems do not capture intent misalignment caused by underspecified input. The absence of clarification increases the risk that the response will be unhelpful or misleading for users with different underlying needs.

## Final Assessment
The response is not evaluation-ready due to insufficient ambiguity handling and failure to clarify user intent before proceeding.

## Improvement Feedback
- Explicitly acknowledge uncertainty in user intent  
- Ask a clarifying question prior to providing a definitive response  
- Offer conditional or scoped guidance that adapts to multiple possible interpretations  

## Why This Case Matters
Underspecified prompts are common in real-world AI usage. Identifying when clarification is required — rather than producing a confident but potentially misaligned answer — is a judgment task that automated metrics and rule-based systems often fail to capture. Human-in-the-loop evaluation is essential for detecting these failure modes.
