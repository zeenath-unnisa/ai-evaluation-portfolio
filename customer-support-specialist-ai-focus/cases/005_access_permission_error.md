## Case ID
_# ACCESS PERMISSION ERROR (Case 005)_

## Customer Message
"Some team members can’t access the AI features even though we’re on the correct plan."

## Category
Access / Permissions

## Context
B2B AI product — role-based access control

## Severity
SEV-2 (High)

## Initial Assessment
- Role-based permission or workspace configuration issue.
- Core functionality blocked for some users.

## Clarifying Questions
- What roles are assigned to the affected users?
- Are they in the correct workspace or organisation?
- When was the last permission change made?

## Draft Customer Response
Thank you for flagging this — I understand how disruptive access issues can be.

AI features are controlled through role-based permissions. I’ll help verify your workspace configuration and ensure the correct access is applied to the affected users as quickly as possible.

## Internal Notes (Support Ops / Engineering)
- Review role-to-feature mappings
- Check org-level feature flags
- Audit recent permission changes

## Escalation Decision
Escalate if permissions appear correct but access issues persist.
