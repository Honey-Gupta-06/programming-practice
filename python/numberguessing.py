import random

number = random.randint(1, 100)
attempts = 0

print("=" * 40)
print("       NUMBER GUESSING GAME")
print("=" * 40)

print("I have selected a number between 1 and 100.")
print("Try to guess it!")

while True:
    try:
        guess = int(input("\nEnter your guess: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")

        elif guess < number:
            print("Too low! Try again.")

        elif guess > number:
            print("Too high! Try again.")

        else:
            print("\n🎉 Congratulations!")
            print(f"You guessed the number in {attempts} attempts.")
            break

    except ValueError:
        print("Please enter a valid number.")