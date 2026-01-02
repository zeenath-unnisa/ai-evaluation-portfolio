## Case ID
_# DATA SYNC FAILURE (Case 002)_

## Customer Message
"Our data hasn’t synced for the past 24 hours, and the AI insights are now outdated. This is affecting our reporting."

## Category
Data Sync / Integration

## Context
B2B AI product — ingestion pipeline supporting analytics and insights

## Severity
SEV-2 (High)

## Initial Assessment
- Likely ingestion or integration failure resulting in stale data being used for AI outputs.
- Impact is moderate to high depending on reporting dependency.
- Initial assessment based on timing and symptom; requires verification of pipeline status and scope.

## Clarifying Questions
- Which data source is affected?
- When was the last successful sync?
- Have there been recent schema or credential changes?
- Is this impacting one workspace or multiple?

## Draft Customer Response
Thank you for reporting this — I understand how critical timely data is for accurate insights and reporting.

It appears the data sync may have stalled, which would explain the outdated outputs. I’ll help confirm where the delay is occurring and work with the team to restore normal syncing as quickly as possible.

## Internal Notes (Engineering / Data)
- Check ingestion pipeline logs
- Validate source credentials
- Confirm schema compatibility
- Review recent deployment changes

## Workaround (If Applicable)
- Manually refresh data if supported
- Pause dependent reporting until sync resumes

## Escalation Decision
Yes - Escalate to data engineering if sync does not resume after validation checks or if multiple customers are affected.
