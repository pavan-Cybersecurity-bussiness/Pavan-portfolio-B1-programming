"A calculator for an bussiness "
# added my style to the sample code
# Get revenue from user

revenue = float(input("Enter total revenue: $ "))
# Get costs from user

costs = float(input("Enter total costs: $ "))

# Calculate profit

profit = revenue - costs

# Calculate profit margin percentage

margin = (profit / revenue) * 100

# Display results

print("--- Financial Summary --- \n everything is give close to 2 significant figures")
print(f"Revenue: ${revenue:,.2f}")
print(f"Costs: ${costs:,.2f}")
if profit < 0 :
    print("You are running a LOSS of : ", -1*profit,"dollars")
print(f"Profit: ${profit:,.2f}")
print(f"Profit Margin: {margin:.1f}%")

