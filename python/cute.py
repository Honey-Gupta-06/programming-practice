import time
import sys

def slow(text, speed=0.035):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def line():
    print("\n" + "═" * 50 + "\n")

print("💻 SECRET PROGRAM v1.0")
time.sleep(1)
slow("Initializing...")
time.sleep(1)
slow("Loading important data...")
time.sleep(1)
slow("Checking user's identity...")
time.sleep(1)

line()

slow("🔐 SECRET ACCESS REQUIRED")
slow("Only one very special person can continue.")
time.sleep(1)

name = input("\nEnter your name: ")

line()

slow("Hmm...")
time.sleep(1)
slow("Scanning...")
time.sleep(1)

slow("Okay... I think I know who you are. ❤️")

time.sleep(1)
line()

slow("Before I give you the secret,")
slow("you have to pass 3 very important tests. 😌")
time.sleep(1)

# Question 1
line()

slow("QUESTION 1 💭")
slow("Who is the cutest person here?")

print("""
1. Me
2. Obviously you
3. This question is unfair 😂
""")

choice = input("Your answer: ")

slow("\nAnalyzing answer...")

if choice == "2":
    slow("Correct. I knew you'd get that one. 😂❤️")
else:
    slow("Wrong answer detected.")
    slow("But I'll forgive you. 😌❤️")

time.sleep(1)

# Question 2
line()

slow("QUESTION 2 💕")
slow("What happens when you make someone smile?")

print("""
1. Nothing
2. You become their favorite person
3. The computer crashes
""")

choice = input("Your answer: ")

slow("\nCalculating...")
time.sleep(1)

if choice == "2":
    slow("Correct! ❤️")
else:
    slow("Interesting answer...")
    slow("I'll pretend that's correct. 😂")

time.sleep(1)

# Question 3
line()

slow("FINAL QUESTION 🔐")
slow("Are you ready to unlock your surprise?")

print("""
1. YES ❤️
2. YESSS 😭❤️
3. Obviously YES
""")

input("Choose your answer: ")

line()

slow("ACCESS GRANTED. 🔓❤️", 0.08)
time.sleep(1)

slow("Decrypting secret message...")
time.sleep(1)
slow("10%...")
time.sleep(0.5)
slow("35%...")
time.sleep(0.5)
slow("67%...")
time.sleep(0.5)
slow("99%...")
time.sleep(0.8)
slow("100%! ❤️")

line()

print("""
        ❤️       ❤️
      ❤️   ❤️ ❤️   ❤️
     ❤️     ❤️     ❤️
      ❤️           ❤️
        ❤️       ❤️
          ❤️   ❤️
            ❤️
""")

time.sleep(1)

slow("SURPRISE! 💌", 0.1)

time.sleep(1)

slow("If you're reading this...")
slow("then you successfully made it through my very serious")
slow("and extremely scientific security system. 😂")

time.sleep(1)

slow("But here's the actual secret... ❤️", 0.06)

time.sleep(1)

slow("You are someone who makes my ordinary days")
slow("feel a little more special.")

time.sleep(1)

slow("And I wanted to turn a tiny piece of code")
slow("into a tiny surprise just for you. 🥹❤️")

time.sleep(1)

slow("So remember...")

time.sleep(1)

slow("YOU + ME = ❤️", 0.1)

line()

slow("💕 END OF PROGRAM 💕", 0.08)
slow("But definitely NOT the end of the story. 😉")

print()