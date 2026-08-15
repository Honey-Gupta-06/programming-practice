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