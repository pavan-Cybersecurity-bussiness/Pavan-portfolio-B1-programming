#Step 1: Initialize Data Structures
expense_records = []
category_totals = {}
unique_categories = set()
#Step 2: Collect Expense Data
num_expenses = int(input("enter number of expense 5 to 7 "))

for i in range(1, num_expenses + 1):
    print(f"Enter expense {i} details:")

    category = input("Category: ")

    # Amount input with validation
    while True:
        try:
            amount = float(input("Amount: $"))
            if amount < 0:
                print("Amount cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Enter a number.")

    date = input("Date (YYYY-MM-DD): ")

    # Append as a tuple
    expense_records.append((category, amount, date))

#Step 3: Categorize and Sum Expenses
for category, amount, date in expense_records:
    unique_categories.add(category)  # set ensures uniqueness

    if category in category_totals:
        category_totals[category] += amount
    else:
        category_totals[category] = amount
#Step 4: Calculate Overall Statistics
amounts = [amount for _, amount, _ in expense_records]

total_spending = sum(amounts)
average_expense = total_spending / len(amounts)
highest_expense = max(amounts)
lowest_expense = min(amounts)

# Find record of highest and lowest expense
highest_record = max(expense_records, key=lambda x: x[1])
lowest_record = min(expense_records, key=lambda x: x[1])

#Step 5: Generate Spending Report
print("\n=== PERSONAL EXPENSE TRACKER ===")

print("\n=== OVERALL SPENDING SUMMARY ===")
print(f"Total Spending: ${total_spending:.2f}")
print(f"Average Expense: ${average_expense:.2f}")
print(f"Highest Expense: ${highest_record[1]:.2f} (Category: {highest_record[0]}, Date: {highest_record[2]})")
print(f"Lowest Expense: ${lowest_record[1]:.2f} (Category: {lowest_record[0]}, Date: {lowest_record[2]})")

print("\n=== UNIQUE CATEGORIES SPENT ON ===")
print(unique_categories)
print(f"Total unique categories: {len(unique_categories)}")

print("\n=== SPENDING BY CATEGORY ===")
for category, total in category_totals.items():
    print(f"{category}: ${total:.2f}")
