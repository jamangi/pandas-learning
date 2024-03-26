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
print(student_101_info)