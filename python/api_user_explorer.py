import requests


API_URL = "https://jsonplaceholder.typicode.com/users"


# Get users from API
def get_users():
    try:
        response = requests.get(API_URL, timeout=10)

        if response.status_code == 200:
            return response.json()

        print("Failed to get users.")
        print("Status Code:", response.status_code)
        return []

    except requests.exceptions.RequestException as error:
        print("Error connecting to API:", error)
        return []


# Show all users
def show_all_users(users):
    if not users:
        print("No users found.")
        return

    print("\n===== ALL USERS =====")

    for user in users:
        print("ID:", user["id"])
        print("Name:", user["name"])
        print("Username:", user["username"])
        print("Email:", user["email"])
        print("City:", user["address"]["city"])
        print("------------------------")


# Search user by name
def search_user(users):
    search_name = input("Enter name to search: ").strip().lower()

    found = False

    for user in users:
        if search_name in user["name"].lower():
            print("\nUser Found!")
            print("ID:", user["id"])
            print("Name:", user["name"])
            print("Username:", user["username"])
            print("Email:", user["email"])
            print("City:", user["address"]["city"])
            found = True

    if not found:
        print("No user found with that name.")


# Show user emails
def show_emails(users):
    if not users:
        print("No users found.")
        return

    print("\n===== USER EMAILS =====")

    for user in users:
        print(user["name"], "→", user["email"])


# Main program
users = get_users()

while True:

    print("\n==============================")
    print("      API USER EXPLORER")
    print("==============================")
    print("1. Show All Users")
    print("2. Search User by Name")
    print("3. Show User Emails")
    print("4. Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_all_users(users)

    elif choice == "2":
        search_user(users)

    elif choice == "3":
        show_emails(users)

    elif choice == "4":
        print("Thank you for using API User Explorer!")
        break

    else:
        print("Invalid choice. Please select 1-4.")