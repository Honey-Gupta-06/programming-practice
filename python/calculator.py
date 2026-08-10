def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

while True:
    print("\n--- Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        result = add(a, b)
        print("Addition of both numbers is:", result)

    elif choice == "2":
        result = subtract(a, b)
        print("Subtraction of both numbers is:", result)

    elif choice == "3":
        result = multiply(a, b)
        print("Multiplication of both numbers is:", result)

    elif choice == "4":
        if b != 0:
            result = divide(a, b)
            print("Division of both numbers is:", result)
        else:
            print("Error: Division by zero!")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")