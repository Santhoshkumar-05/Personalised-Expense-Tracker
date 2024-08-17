import datetime

# Initialize an empty list to store expenses
expenses = []

# Function to add an expense
def add_expense(date, category, description, amount):
    expense = {
        'date': date,
        'category': category,
        'description': description,
        'amount': amount
    }
    expenses.append(expense)
    print("Expense added successfully!")

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. Date: {expense['date']}, Category: {expense['category']}, Description: {expense['description']}, Amount: ${expense['amount']:.2f}")

# Function to get a summary report
def get_summary():
    if not expenses:
        print("No expenses recorded yet.")
        return
    summary = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    print("Expense Summary by Category:")
    for category, total_amount in summary.items():
        print(f"{category}: ${total_amount:.2f}")

# Function to interact with the user
def main():
    print("Welcome to the Expense Tracker!")
    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Get Summary Report")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category (e.g., Food, Transport, etc.): ")
            description = input("Enter a description: ")
            amount = float(input("Enter the amount: "))
            add_expense(date, category, description, amount)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            get_summary()
        elif choice == '4':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
