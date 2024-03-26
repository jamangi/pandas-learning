# pandas-learning
pandas-learning

Panda things to learn:
### How to create DataFrames - Pandas Data Structures
- What shape must the raw data model be in
- How can the raw data model be put into a DataFrame
- How to create a new column based on an old column

- Looks like the data model can either be a list of lists or a dict of lists
  - If it's a list of lists, each sub-list must have the same shape,
  - If it's a dict of lists, the dict can be put into the DataFrame constructor without specifying column names (the keys are column names)
### How to read DataFrames - Data Inspection
- reading metadata, such as number of rows and columns 
- reading the first three rows
- read row according to a select filter
- read specific columns of a row selected by filter
### How to Delete data - Data Cleaning
- How to delete duplicate rows in which data in one column is duplicated
- How to delete rows with no data in some particular column
## How to Update data - Data Cleaning & Table Reshaping
- How to modify the data in a column
- How to rename columns of data

# CREATE
dict of lists:
```py
import pandas as pd
persondata = {'personId': [1, 2], 'lastName': ['Wang', 'Alice'], 'firstName': ['Allen', 'Bob']} 
addressdata = {'addressId': [1, 2], 'personId': [1, 2], 'city': ['New York City', 'Leetcode'], 'state': ['New York', 'California']} 
Person = pd.DataFrame(persondata)
Address = pd.DataFrame(addressdata)


# Another Example

data = {
    'A': [1, 2, 3, 4, 5],
    'B': ['a', 'b', 'c', 'd', 'e'],
    'C': [True, False, True, False, True]
}
df = pd.DataFrame(data)
```

list of lists:
```py
import pandas as pd
data = [[1, 'Wang', 'Allen'], [2, 'Alice', 'Bob']]
person = pd.DataFrame(data, columns=['personId', 'firstName', 'lastName']).astype({'personId':'Int64', 'firstName':'object', 'lastName':'object'})
data = [[1, 2, 'New York City', 'New York'], [2, 3, 'Leetcode', 'California']]
address = pd.DataFrame(data, columns=['addressId', 'personId', 'city', 'state']).astype({'addressId':'Int64', 'personId':'Int64', 'city':'object', 'state':'object'})
```

list of dicts:
```py
pd = pd.DataFrame([{"name": "bob", "salary": 200}, {"name": "joe", "salary": 500}])
```

Creating a new column based on an old column
```py 
import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees
```


# READ
reading metadata, such as number of rows and columns:
```py
import pandas as pd

def getDataframeSize(players: pd.DataFrame):
    rows, cols = players.shape
    return [rows, cols]
```

reading the first three rows:
```py
import pandas as pd

# Assuming df is your DataFrame
# Example DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': ['a', 'b', 'c', 'd', 'e'],
    'C': [True, False, True, False, True]
}
df = pd.DataFrame(data)

# Display the first three rows
first_three_rows = df.head(3)
print(first_three_rows)
```

read row according to a select filter:
```py 
import pandas as pd

# Assuming df is your DataFrame
# Example DataFrame
data = {
    'Student_ID': [101, 102, 103],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [20, 21, 22]
}
df = pd.DataFrame(data)

# Select the row with Student_ID = 101
student_101_row = df[df['Student_ID'] == 101]
print(student_101_row)
```

read specific columns of a row selected by filter:
```py 
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
```
As you can see, a DF has a boolean indexer, '[]' similar to a list's index, but it can take a df or a list as input.
# Delete

Deletes the entire row containing the duplicate data in only the email column
```py
import pandas as pd

# Assuming df is your DataFrame
# Example DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Email': ['alice@example.com', 'bob@example.com', 'alice@example.com', 'david@example.com', 'emma@example.com']
}
df = pd.DataFrame(data)

# Drop rows with duplicate emails, keeping only the first occurrence
df_unique_emails = df.drop_duplicates(subset=['Email'], keep='first')

# Print the DataFrame after dropping duplicates
print(df_unique_emails)
```

How to delete rows with no data in some particular column:
```py
df_cleaned = df.dropna(subset=['Name'])
```

# Update
How to modify the data in a column:
```py
import pandas as pd
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees

pd = pd.DataFrame([{"name": "bob", "salary": 200}, {"name": "joe", "salary": 500}])
print(pd)
```

How to rename columns of data:
```py
import pandas as pd

# Assuming df is your DataFrame
# Example DataFrame
data = {
    'id': [1, 2, 3],
    'first': ['Alice', 'Bob', 'Charlie'],
    'last': ['Smith', 'Doe', 'Brown'],
    'age': [25, 30, 35]
}
df = pd.DataFrame(data)

df_renamed = df.rename(columns={'id': 'student_id', 'first': 'first_name', 'last': 'last_name', 'age': 'age_in_years'})
```