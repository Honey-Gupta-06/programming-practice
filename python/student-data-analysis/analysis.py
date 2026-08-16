import pandas as pd
import matplotlib.pyplot as plt


# ==========================
# 1. Load Dataset
# ==========================

df = pd.read_csv("data/students.csv")

print("===== STUDENT DATA =====")
print(df)


# ==========================
# 2. Dataset Information
# ==========================

print("\n===== DATASET INFORMATION =====")

print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

print("\nColumns:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)


# ==========================
# 3. Check Missing Values
# ==========================

print("\n===== MISSING VALUES =====")

print(df.isnull().sum())


# ==========================
# 4. Calculate Total Marks
# ==========================

df["Total"] = (
    df["Math"]
    + df["Science"]
    + df["Computer"]
)

df["Percentage"] = df["Total"] / 3

print("\n===== STUDENT RESULTS =====")

print(
    df[
        [
            "Name",
            "Total",
            "Percentage"
        ]
    ]
)


# ==========================
# 5. Average Marks
# ==========================

print("\n===== AVERAGE MARKS =====")

print("Math:", df["Math"].mean())
print("Science:", df["Science"].mean())
print("Computer:", df["Computer"].mean())


# ==========================
# 6. Top Student
# ==========================

top_student = df.loc[df["Percentage"].idxmax()]

print("\n===== TOP STUDENT =====")

print("Name:", top_student["Name"])
print("Percentage:", top_student["Percentage"])


# ==========================
# 7. Students Above 80%
# ==========================

print("\n===== STUDENTS ABOVE 80% =====")

high_performers = df[df["Percentage"] > 80]

print(
    high_performers[
        ["Name", "Percentage"]
    ]
)


# ==========================
# 8. Average Marks by Course
# ==========================

print("\n===== AVERAGE BY COURSE =====")

course_average = df.groupby("Course")["Percentage"].mean()

print(course_average)


# ==========================
# 9. Average Marks by City
# ==========================

print("\n===== AVERAGE BY CITY =====")

city_average = df.groupby("City")["Percentage"].mean()

print(city_average)


# ==========================
# 10. Bar Chart
# ==========================

course_average.plot(kind="bar")

plt.title("Average Percentage by Course")
plt.xlabel("Course")
plt.ylabel("Average Percentage")

plt.tight_layout()
plt.show()


# ==========================
# 11. Histogram
# ==========================

plt.hist(df["Percentage"], bins=5)

plt.title("Distribution of Student Percentage")
plt.xlabel("Percentage")
plt.ylabel("Number of Students")

plt.tight_layout()
plt.show()


# ==========================
# 12. Scatter Plot
# ==========================

plt.scatter(
    df["Math"],
    df["Computer"]
)

plt.title("Math vs Computer Marks")
plt.xlabel("Math Marks")
plt.ylabel("Computer Marks")

plt.tight_layout()
plt.show()