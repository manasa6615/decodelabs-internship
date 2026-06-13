total = 0
print("--- Expense Tracker ---")
print("Enter your expenses one by one.")
print("Type 'done' to see the final total and exit.")
while True:
    user_input = input("Enter expense amount: ")
    if user_input.lower() == 'done':
        break
    try:
        expense = float(user_input)
        total += expense
        print(f"Current Total: ${total:.2f}")
        
    except ValueError:
        print("Invalid Data. Please enter a numerical amount.")
print("-" * 20)
print(f"FINAL TOTAL SPENT: ${total:.2f}")
print("Thank you for using the Expense Tracker!")