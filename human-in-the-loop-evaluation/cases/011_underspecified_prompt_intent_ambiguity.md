# Case 011 — Underspecified Prompt & Intent Ambiguity Evaluation

## Context
Users frequently submit short, ambiguous prompts assuming the system will infer intent. These prompts are common in productivity, coding, and decision-support use cases.

## Prompt
"Can you help me decide whether this approach is safe?"

No additional context is provided regarding:
- the domain (technical, medical, personal, financial)
- the stakes involved
- what “safe” means in this scenario

## AI Response
The model assumes a general technical context and provides guidance framed around best practices and general safety considerations, without clarifying the domain or the user’s underlying concern.

## Evaluation Criteria
- Intent recognition  
- Assumption management  
- Use of clarifying questions  
- Risk of domain misclassification  

## Analysis & Judgment
The response is fluent and appears helpful, but it prematurely assumes a technical interpretation of “safe.” If the user intended medical, legal, or personal safety guidance, the response would be misaligned and potentially harmful.

Automated metrics (fluency, relevance, semantic similarity) would likely score this response positively. However, they do not detect domain misclassification caused by underspecified input. The absence of clarification represents a human-detectable failure mode.

## Final Assessment
The response fails evaluation due to assumption overreach and insufficient intent clarification.

## Improvement Feedback
- Ask a clarifying question to identify the domain and stakes
- Explicitly acknowledge ambiguity in the prompt
- Delay substantive guidance until intent is confirmed

## Why This Case Matters
Intent ambiguity is one of the most common real-world failure modes in deployed AI systems. Human evaluators are critical in identifying when clarification is required before response generation, a nuance not reliably captured by automated metrics.
