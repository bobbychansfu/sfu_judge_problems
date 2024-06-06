
goal = int(input("Enter your savings goal: "))

total_savings = 0
weeks = 0

while total_savings < goal:
    weekly_savings = int(input(f"Enter your savings for week {weeks + 1}: "))
    total_savings += weekly_savings
    weeks += 1

print(f"Congratulations! Number of weeks to reach your goal: {weeks}")
