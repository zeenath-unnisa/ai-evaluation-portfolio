def assign_priority(customer_type, issue_type, tickets_open):
    customer_type = customer_type.strip().lower()
    issue_type = issue_type.strip().lower()

    valid_customer_types = {"premium", "standard", "trial"}
    valid_issue_types = {"billing", "login", "bug"}

    if customer_type not in valid_customer_types:
        raise ValueError(f"Invalid customer_type: {customer_type}")
    if issue_type not in valid_issue_types:
        raise ValueError(f"Invalid issue_type: {issue_type}")
    if tickets_open < 0:
        raise ValueError("tickets_open must be >= 0")

    # Base priority
    if customer_type == "premium":
        priority = "P2 - High"
    elif customer_type == "standard":
        priority = "P3 - Medium"
    else:  # trial
        priority = "P4 - Low"

    # Escalation when queue is high
    if tickets_open >= 10:
        if customer_type == "premium":
            priority = "P1 - Critical"
        elif customer_type == "standard":
            priority = "P2 - High"
        else:  # trial
            priority = "P3 - Medium"

    return priority

# Test harness (like you already did)
customer_types = ["premium", "standard", "trial"]
issue_types = ["billing", "login", "bug"]
ticket_counts = list(range(1, 15))

for ct in customer_types:
    for it in issue_types:
        for t in ticket_counts:
            print(ct, it, t, "=>", assign_priority(ct, it, t))
