import pandas as pd

# Assuming df is your DataFrame
# Example DataFrame
data = {
    'Student_ID': [101, 102, 103],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [20, 21, 22]
}
df = pd.DataFrame(data)

# Select name and age of the student with Student_ID = 101
student_101_info = df[df['Student_ID'] == 101][['Name', 'Age']]
print()
print(df) # pritns the column names, the row numbers, and all column data
print("*"*40)
print(df['Student_ID']) # prints the row numbers, and only the student_id column data
print("*"*40)
print(df[df['Student_ID'] == 101]) # prints all column names, prints row number, all column info where student id == 101 - produces a df
print("*"*40)
print(df[['Student_ID']]) # like df['Student_ID'], but includes column name
print("*"*40)
print(df['Student_ID'] == 101) # this shows the row ids, but the column data is all trues and falses. It's a truth table based on ['Student_ID'] == 101
print("*"*40)
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees

df = pd.DataFrame([{"name": "bob", "salary": 200}, {"name": "joe", "salary": 500}])
modifySalaryColumn(df)
print(df)

print("*"*40)
data = {
    'city': ['CityA', 'CityB', 'CityA', 'CityB', 'CityA', 'CityB'],
    'month': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar', 'Mar'],
    'temperature': [10, 15, 12, 14, 11, 16]
}
df = pd.DataFrame(data)

# Pivot the DataFrame
pivot_df = df.pivot_table(index='month', columns='city', values='temperature')

# Print the pivoted DataFrame
print(pivot_df)
print("*"*40)
pivot_df = pivot_df.astype(int)
print(pivot_df)

pivot_df = df.pivot(index='month', columns='city', values='temperature')
print("*"*40)
print(pivot_df)