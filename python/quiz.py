questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web page structure?",
        "options": ["A. Python", "B. Java", "C. HTML", "D. SQL"],
        "answer": "C"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. int", "B. bool", "C. str", "D. float"],
        "answer": "B"
    },
    {
        "question": "What is 10 + 20?",
        "options": ["A. 20", "B. 25", "C. 30", "D. 40"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
    }
]


def run_quiz():
    score = 0

    print("=" * 40)
    print("       PYTHON QUIZ APPLICATION")
    print("=" * 40)

    for number, question in enumerate(questions, start=1):
        print(f"\nQuestion {number}: {question['question']}")

        for option in question["options"]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is {question['answer']}.")

    print("\n" + "=" * 40)
    print("              QUIZ RESULT")
    print("=" * 40)

    print(f"Your score: {score}/{len(questions)}")

    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.2f}%")

    if percentage == 100:
        print("Excellent!")
    elif percentage >= 60:
        print("Good job!")
    elif percentage >= 40:
        print("Keep practicing!")
    else:
        print("You need more practice.")

    print("=" * 40)


run_quiz()