import requests


def get_quote():
    url = "https://dummyjson.com/quotes/random"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()

            print("\n==============================")
            print("        RANDOM QUOTE")
            print("==============================")
            print("Quote:", data["quote"])
            print("Author:", data["author"])
            print("==============================")

        else:
            print("Unable to get quote.")
            print("Status code:", response.status_code)

    except requests.exceptions.RequestException:
        print("Network error. Please check your internet connection.")


while True:

    print("\n===== QUOTE APP =====")
    print("1. Get Random Quote")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        get_quote()

    elif choice == "2":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")