import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


print("=" * 40)
print("       PASSWORD GENERATOR")
print("=" * 40)

try:
    length = int(input("Enter password length: "))

    if length < 4:
        print("Password length should be at least 4.")
    else:
        password = generate_password(length)

        print("\nGenerated Password:")
        print(password)

except ValueError:
    print("Please enter a valid number.")