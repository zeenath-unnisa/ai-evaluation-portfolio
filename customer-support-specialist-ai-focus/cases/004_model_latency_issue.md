## Case ID
_# MODEL LATENCY ISSUE (Case 004)_

## Customer Message
"AI responses are taking over 30 seconds today, which is breaking our workflow."

## Category
Performance / Latency

## Context
B2B AI product — response time degradation affecting workflows

## Severity
SEV-2 (High)

## Initial Assessment
- Likely performance degradation impacting inference response times.
- Possible contributing factors include increased load, regional traffic spikes, or upstream service delays.
- Initial assessment based on reported latency; scope and impact need confirmation.

## Clarifying Questions
- When did the latency start (time and timezone)?
- What is the usual response time vs current?
- Is the issue affecting all users or specific roles?
- Does it occur across all features or a single workflow?
- Are errors or timeouts also occurring?

## Draft Response
Thanks for reporting this — I understand how disruptive latency can be for time-sensitive workflows.

We’re currently investigating increased response times. I’d like to gather a few details to determine whether this is isolated or part of a broader performance issue. I’ll keep you updated as we learn more.

## Internal Notes
- Review latency metrics
- Check regional traffic patterns
- Cross-reference incident dashboard

## Workaround (If Applicable)
- Retry requests after a short interval
- Avoid peak usage periods where possible
- Reduce request complexity temporarily

## Escalation Decision
Yes — escalate if latency persists, affects multiple customers, or exceeds agreed SLAs.
