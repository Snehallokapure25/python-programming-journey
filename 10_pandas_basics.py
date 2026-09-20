import pandas as pd

data = {
    "Name": ["Snehal", "Aditi", "Anushka"],
    "Age": [20, 20, 19],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())
