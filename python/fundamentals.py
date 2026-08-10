# Student Grade Calculator

name = input("Enter student name: ")

math = float(input("Enter Math marks: "))
science = float(input("Enter Science marks: "))
computer = float(input("Enter Computer marks: "))

total = math + science + computer
percentage = total / 3

print("\n----- Student Result -----")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)