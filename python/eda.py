import pandas as pd
df = pd.read_csv("python/student_data.csv")

print("Student Data:")
print(df)
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nBasic Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStudents scoring above 80:")
print(df[df["Marks"] > 80])

print("\nStudents from Ranchi:")
print(df[df["City"] == "Ranchi"])

average_marks = df["Marks"].mean()
print("\nAverage Marks:", average_marks)

print("Highest Marks:", df["Marks"].max())

print("Lowest Marks:", df["Marks"].min())

print("\nAverage Marks by Course:")
print(df.groupby("Course")["Marks"].mean())

print("\nAverage Marks by City:")
print(df.groupby("City")["Marks"].mean())

