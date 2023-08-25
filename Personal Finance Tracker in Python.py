# Personal Finance Tracker in Python

# Initialize empty lists for income and expenses
income = []
expenses = []

# Function to record income
def record_income():
    amount = float(input("Enter income amount: "))
    income.append(amount)
    print(f"Income of ${amount} recorded.")

# Function to record expenses
def record_expense():
    amount = float(input("Enter expense amount: "))
    expenses.append(amount)
    print(f"Expense of ${amount} recorded.")

# Function to calculate and display summary
def display_summary():
    total_income = sum(income)
    total_expenses = sum(expenses)
    balance = total_income - total_expenses
    
    print("\n---- Summary ----")
    print(f"Total Income: ${total_income}")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Balance: ${balance}")

# Main loop for the finance tracker
while True:
    print("\nPersonal Finance Tracker Menu:")
    print("1. Record Income")
    print("2. Record Expense")
    print("3. Display Summary")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        record_income()
    elif choice == '2':
        record_expense()
    elif choice == '3':
        display_summary()
    elif choice == '4':
        print("Exiting the Finance Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
