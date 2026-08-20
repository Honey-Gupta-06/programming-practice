import random

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
        "answer": "New Delhi"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Mercury"],
        "answer": "Mars"
    },
    {
        "question": "Who wrote the Indian national anthem?",
        "options": [
            "Rabindranath Tagore",
            "Bankim Chandra Chattopadhyay",
            "Sarojini Naidu",
            "Subhas Chandra Bose"
        ],
        "answer": "Rabindranath Tagore"
    },
    {
        "question": "Which is the largest ocean in the world?",
        "options": [
            "Atlantic Ocean",
            "Indian Ocean",
            "Pacific Ocean",
            "Arctic Ocean"
        ],
        "answer": "Pacific Ocean"
    },
    {
        "question": "How many continents are there in the world?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "Which gas do plants absorb during photosynthesis?",
        "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"],
        "answer": "Carbon dioxide"
    },
    {
        "question": "Which is the largest planet in our Solar System?",
        "options": ["Earth", "Saturn", "Jupiter", "Neptune"],
        "answer": "Jupiter"
    },
    {
        "question": "Who was the first person to walk on the Moon?",
        "options": [
            "Yuri Gagarin",
            "Neil Armstrong",
            "Buzz Aldrin",
            "Michael Collins"
        ],
        "answer": "Neil Armstrong"
    },
    {
        "question": "Which is the longest river in India?",
        "options": ["Yamuna", "Ganga", "Godavari", "Narmada"],
        "answer": "Ganga"
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["Won", "Yuan", "Yen", "Ringgit"],
        "answer": "Yen"
    }
]


def start_quiz():

    score = 0

    # Select 5 UNIQUE random questions
    selected_questions = random.sample(questions, 5)

    print("\n================================")
    print("        RANDOM GK QUIZ")
    print("================================")

    for number, q in enumerate(selected_questions, 1):

        print(f"\nQuestion {number}:")
        print(q["question"])

        # Shuffle options
        options = q["options"].copy()
        random.shuffle(options)

        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        while True:
            try:
                choice = int(input("\nYour answer (1-4): "))

                if 1 <= choice <= 4:
                    break

                print("Enter a number between 1 and 4.")

            except ValueError:
                print("Please enter a valid number.")

        if options[choice - 1] == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")

    print("\n================================")
    print("          QUIZ RESULT")
    print("================================")
    print(f"Score: {score}/5")
    print(f"Percentage: {score * 20}%")
    print("================================")


# Keep playing
while True:

    start_quiz()

    again = input("\nPlay another quiz? (yes/no): ").lower()

    if again != "yes":
        print("\nThanks for playing! 👋")
        break