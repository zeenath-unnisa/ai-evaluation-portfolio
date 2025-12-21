# Day 4 - Fuctions and compound logic



tickets_open = 5
customer_type = "trial" # premium, standard, trial
issue_type = "billing"        # billing, login, bug


if customer_type == "premium" and issue_type == "billing" and tickets_open >= 10:
    priority = "P1 - Critical"
elif customer_type == "premium" and issue_type == "billing" and tickets_open < 10:
    priority = "P2 - High"
elif customer_type == "standard" and issue_type == "billing" and tickets_open >= 10:
    priority = "P2 - High"
elif customer_type == "standard" and issue_type == "billing" and tickets_open < 10:
    priority = "P3 - Medium"
elif customer_type == "premium" and issue_type == "login" and tickets_open >= 10:
    priority = "P1 - Critical"
elif customer_type == "premium" and issue_type == "login" and tickets_open < 10:
    priority = "P2 - High"
elif customer_type == "premium" and issue_type == "bug" and tickets_open >= 10:
    priority = "P1 - Critical"
elif customer_type == "premium" and issue_type == "bug" and tickets_open < 10:
    priority = "P2 - High"
elif customer_type == "standard" and issue_type == "login" and tickets_open >= 10:
    priority = "P2 - High"
elif customer_type == "standard" and issue_type == "login" and tickets_open < 10:
    priority = "P3 - Medium"
elif customer_type == "standard" and issue_type == "bug" and tickets_open >= 10:
    priority = "P2 - High"
elif customer_type == "standard" and issue_type == "bug" and tickets_open < 10:
    priority = "P3 - Medium"
elif customer_type == "trial" and tickets_open > 10:
    priority = "P3 - Medium"
else:
    priority = "P4 - Low"

print("Tickets open:", tickets_open)
print("Customer_type:", customer_type)
print("Issue type:", issue_type)
print("Assigned priority:", priority)
