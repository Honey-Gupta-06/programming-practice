import pandas as pd


data = {
    "Name": ["Honey", "Rahul", "Anjali", "Priya"],
    "Age": [20, 21, 19, 20],
    "Marks": [85, 78, 92, 88],
    "Course": ["ITM", "BCA", "ITM", "BSc"]
}


df = pd.DataFrame(data)

print("===== STUDENT DATA =====")
print(df)

print("\n===== FIRST 2 STUDENTS =====")
print(df.head(2))

print("\n===== STUDENT NAMES =====")
print(df["Name"])

print("\n===== MARKS =====")
print(df["Marks"])

print("\n===== AVERAGE MARKS =====")
print(df["Marks"].mean())

print("\n===== HIGHEST MARKS =====")
print(df["Marks"].max())

print("\n===== LOWEST MARKS =====")
print(df["Marks"].min())