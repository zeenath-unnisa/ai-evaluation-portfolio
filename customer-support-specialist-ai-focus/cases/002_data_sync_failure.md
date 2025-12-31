## Case ID
_# DATA SYNC FAILURE (Case 002)_

## Customer Message
"Our data hasn’t synced for the past 24 hours, and the AI insights are now outdated. This is affecting our reporting."

## Category
Data Sync / Integration

## Severity
SEV-2 (High)

## Initial Assessment
- Data pipeline failure causing stale or incomplete AI outputs.
- Business reporting impacted.

## Clarifying Questions
- Which data source is affected?
- When did the last successful sync occur?
- Have there been recent schema or credential changes?
- Is this impacting one workspace or multiple?

## Draft Customer Response
Thank you for reporting this — I understand how critical timely data is for accurate AI insights and reporting.

It looks like the data sync may have stalled, which would explain the outdated outputs. I’d like to confirm a few details so we can identify whether this is a connection issue, a configuration change, or a system delay.
I’ll keep you updated as we investigate and work toward restoring normal sync behaviour.

## Internal Notes (Engineering / Data)
- Check ingestion pipeline logs
- Validate source credentials
- Confirm schema compatibility
- Review recent deployment changes

## Escalation Decision
Escalate to data engineering if sync does not resume after validation checks or if multiple customers are affected.
