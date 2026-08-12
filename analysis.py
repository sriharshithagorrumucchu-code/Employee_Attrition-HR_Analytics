import pandas as pd

# Read CSV file
df = pd.read_csv("employee_attrition.csv")

# Display data
print("Employee Data")
print(df)

# Display first 5 rows
print("\nFirst 5 Rows")
print(df.head())

# Display information
print("\nDataset Information")
print(df.info())

# Display statistics
print("\nStatistics")
print(df.describe())

# Count employees who left
print("\nAttrition Count")
print(df["Attrition"].value_counts())