## Case ID
_# MODEL LATENCY ISSUE (Case 004)_

## Customer Message
"AI responses are taking over 30 seconds today, which is breaking our workflow."

## Category
Performance / Latency

## Context
B2B AI product — response time degradation affecting customer workflows

## Severity
SEV-2 (High)

## Initial Assessment
Likely performance degradation impacting inference latency. Possible causes include increased regional load, rate limiting, degraded upstream dependencies, or an active incident affecting model serving. Initial assessment based on limited information; scope and impact need confirmation.

## Clarifying Questions
- When did the latency start (approximate time and timezone)?
- What is the typical response time vs what you’re seeing now (e.g., 5s → 30s)?
- Is the issue affecting all users in your organisation or only specific users?
- Does the latency occur across all features (chat, report generation, API) or only one workflow?
- Which region or location are the affected users in?
- Are you seeing timeouts or errors as well, or only slow responses?
- Have there been any recent changes (new integrations, increased usage, automation, scheduled jobs)?
- If using the API, can you share request IDs or timestamps for slow requests?

## Draft Response
Thanks for reporting this. I understand how delays like this can interrupt time-sensitive workflows.
We’re currently investigating elevated response times and working to determine whether this is an isolated issue or part of a broader performance degradation. In the meantime, I’d like to gather a few details to help us narrow down the cause and prioritise the fix.
I’ll keep you updated as soon as we have more information.

## Internal Notes (Engineering / Ops)
- Check model serving and inference latency metrics
- Review regional traffic and load patterns
- Validate rate-limiting and throttling behaviour
- Cross-reference incident dashboard and recent deployments

## Workaround (If Applicable)
- Retry requests after a short interval
- Avoid peak usage periods if possible
- Reduce prompt size or batch requests temporarily (if supported)
- Apply documented best practices until the issue is resolved

## Escalation Decision
Yes — escalate if latency persists, affects multiple customers, or exceeds agreed SLAs.
