FILE_NAME = "expenses.txt"


def add_expense():
    amount = float(input("Enter expense amount: "))

    with open(FILE_NAME, "a") as file:
        file.write(str(amount) + "\n")

    print("Expense added successfully!")


def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            expenses = file.readlines()

        if not expenses:
            print("No expenses found.")
            return

        print("\nYour Expenses:")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. ₹{float(expense.strip()):.2f}")

    except FileNotFoundError:
        print("No expenses found yet.")


def show_total():
    try:
        with open(FILE_NAME, "r") as file:
            expenses = file.readlines()

        total = sum(float(expense.strip()) for expense in expenses)

        print(f"\nTotal expenses: ₹{total:.2f}")

    except FileNotFoundError:
        print("Total expenses: ₹0.00")


while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        show_total()

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")