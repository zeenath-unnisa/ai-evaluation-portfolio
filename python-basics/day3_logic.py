# Day 3 - Basic logic with if / elif / else

# Imagine we classify ticket priority based on impact

tickets_open = 8
customer_type = "paying"   # options: "trial" or "paying"
issue_type = "bug"       # e.g. "login", "billing", "bug"

# Simple rule-based priority
if customer_type == "paying" and issue_type == "billing":
    priority = "P1 - Critical"
elif customer_type == "paying" and issue_type == "login":
    priority = "P2 - High"
elif customer_type == "paying" and issue_type == "bug":
    priority = "P2 - High"
elif customer_type == "trial" and issue_type == "login":
    priority = "P3 - Medium"
else:
    priority = "P4 - Low"

print("Tickets open:", tickets_open)
print("Customer type:", customer_type)
print("Issue type:", issue_type)
print("Assigned priority:", priority)
