## Case ID
007

## Customer Message
"Our team members can’t access the AI features even though we’re on the correct plan."

## Category
Access / Permissions

## Severity
SEV-2 (High)

## Initial Assessment
Likely role-based permission or workspace configuration issue.
Blocking core functionality.

## Clarifying Questions
- What role is assigned to the affected users?
- Are they in the correct workspace or org?
- When did the issue first appear?

## Draft Customer Response
Thanks for flagging this. Access issues like this can be frustrating, especially when features are expected to be available.
AI features are controlled by role-based permissions. I’ll help verify your workspace configuration and ensure the correct access is applied.

## Internal Notes (Engineering / Support Ops)
- Check role-to-feature mapping
- Verify org-level feature flags
- Review recent permission changes

## Escalation Decision
Escalate if configuration appears correct but access is still blocked.
