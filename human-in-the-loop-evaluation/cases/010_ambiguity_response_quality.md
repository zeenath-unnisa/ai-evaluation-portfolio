## Case 010 — Ambiguity & Response Quality Evaluation

### Context
The user provides an underspecified prompt that can be interpreted in multiple ways.

### Prompt
The input lacks sufficient detail to confidently determine user intent.

### AI Response
The model selects one interpretation and provides a complete response based on that assumption.

### Evaluation Criteria
- Assumption management
- Clarifying question usage
- Alignment with possible user intents
- Response completeness

### Analysis & Judgment
While the response is coherent, it prematurely commits to an interpretation without confirming intent. This introduces a risk of misalignment and reduces usefulness for users with different underlying needs.

### Final Assessment
The response is directionally helpful but fails to manage ambiguity appropriately.

### Improvement Feedback
- Ask a clarifying question before proceeding
- Acknowledge multiple possible interpretations
- Provide conditional guidance where appropriate

### Why This Case Matters
Ambiguity handling is a core area where human judgment adds value. Effective evaluation helps prevent subtle misalignment that automated systems often miss.
