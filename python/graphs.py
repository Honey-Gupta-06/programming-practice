import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("python/student_data.csv")

# Display the data
print("Student Data:")
print(df)


# -----------------------------
# 1. Bar Graph
# -----------------------------

course_marks = df.groupby("Course")["Marks"].mean()

course_marks.plot(kind="bar")

plt.title("Average Marks by Course")
plt.xlabel("Course")
plt.ylabel("Average Marks")
plt.tight_layout()

plt.show()


# -----------------------------
# 2. Line Graph
# -----------------------------

plt.plot(df["Name"], df["Marks"], marker="o")

plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# -----------------------------
# 3. Histogram
# -----------------------------

plt.hist(df["Marks"], bins=5)

plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.tight_layout()

plt.show()