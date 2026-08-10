expenses = []

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter expense amount: "))
        expenses.append(amount)
        print("Expense added!")

    elif choice == "2":
        print("\nYour expenses:")
        for expense in expenses:
            print("₹", expense)

    elif choice == "3":
        print("Total expenses: ₹", sum(expenses))

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")