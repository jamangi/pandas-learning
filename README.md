# pandas-learning
pandas-learning

Tutorial: https://leetcode.com/studyplan/introduction-to-pandas/

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
- how to method chain, to filter, order, and select in one line
### How to Delete data - Data Cleaning
- How to delete duplicate rows in which data in one column is duplicated
- How to delete rows with no data in some particular column
## How to Update data - Data Cleaning & Table Reshaping
- How to modify the data in a column
- How to rename columns of data
- How to change the data-type of a column's data
- How to replace null values with some other value
- How to concatenate two DataFrames vertically into one DataFrame
- How to pivot data, to turn duplicate horizontal values into vertical columns
- How to reshape the data, from more columns to less columns

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

How to method chain, to filter, order, and select in one line:
```py
import pandas as pd

# Assuming df is your DataFrame
# Example DataFrame
data = {
    'name': ['Lion', 'Elephant', 'Giraffe', 'Tiger', 'Hippo'],
    'species': ['Mammal', 'Mammal', 'Mammal', 'Mammal', 'Mammal'],
    'age': [5, 10, 8, 6, 4],
    'weight': [200, 5000, 800, 150, 300]
}
df = pd.DataFrame(data)

# List names of animals that weigh more than 100 kilograms, sorted by weight in descending order
result = (
    df[df['weight'] > 100]  # Filter animals with weight > 100 kilograms
    .sort_values(by='weight', ascending=False)  # Sort by weight in descending order
    ['name']  # Select only the 'name' column
    .tolist()  # Convert the Series to a list
)

print(result)

# OR

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals['weight'] > 100].sort_values(by='weight', ascending=False)[['name']]

```
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

How to change the data-type of a column's data:
```py
import pandas as pd

# Assuming df is your DataFrame
# Example DataFrame
data = {
    'student_id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [20, 21, 22],
    'grade': [85.5, 90.3, 88.7]
}
df = pd.DataFrame(data)

# Convert the "grade" column from float to integer
df['grade'] = df['grade'].astype(int)

# Print the DataFrame after conversion
print(df)
```
How to replace null values with some other value:
```py
import pandas as pd

# Assuming df is your DataFrame
# Example DataFrame
data = {
    'name': ['Product A', 'Product B', 'Product C', 'Product D'],
    'quantity': [10, None, 20, None],
    'price': [15.99, 20.50, 10.25, 5.75]
}
df = pd.DataFrame(data)

# Fill missing values in the "quantity" column with 0
df['quantity'].fillna(0, inplace=True)

# Print the DataFrame after filling missing values
print(df)
```

How to concatenate two DataFrames vertically into one DataFrame
```py
import pandas as pd

# Assuming df1 and df2 are your DataFrames
# Example DataFrames
data1 = {
    'student_id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [20, 21, 22]
}
data2 = {
    'student_id': [4, 5, 6],
    'name': ['David', 'Emma', 'Frank'],
    'age': [23, 24, 25]
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Concatenate the DataFrames vertically
result_df = pd.concat([df1, df2], ignore_index=True)

# Print the concatenated DataFrame
print(result_df)
```

How to pivot data, to turn duplicate horizontal values into vertical columns
```py
import pandas as pd

# Assuming df is your DataFrame
# Example DataFrame
data = {
    'city': ['CityA', 'CityB', 'CityA', 'CityB', 'CityA', 'CityB'],
    'month': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar', 'Mar'],
    'temperature': [10, 15, 12, 14, 11, 16]
}
df = pd.DataFrame(data)

# Pivot the DataFrame
pivot_df = df.pivot_table(index='month', columns='city', values='temperature').astype(int)

# Print the pivoted DataFrame
print(pivot_df)
```
```pycon
city   CityA  CityB

month              
Feb       12     14
Jan       10     15
Mar       11     16
```

How to reshape the data, from more columns to less columns:
```py
import pandas as pd

# Assuming df is your DataFrame
# Example DataFrame
data = {
    'product': ['ProductA', 'ProductB', 'ProductC'],
    'quarter_1': [100, 200, 300],
    'quarter_2': [150, 250, 350],
    'quarter_3': [200, 300, 400],
    'quarter_4': [250, 350, 450]
}
df = pd.DataFrame(data)

# Reshape the DataFrame
reshaped_df = df.melt(id_vars='product', var_name='quarter', value_name='sales')

# Print the reshaped DataFrame
print(reshaped_df)
```
```pycon
    product    quarter  sales
0  ProductA  quarter_1    100
1  ProductB  quarter_1    200
2  ProductC  quarter_1    300
3  ProductA  quarter_2    150
4  ProductB  quarter_2    250
5  ProductC  quarter_2    350
6  ProductA  quarter_3    200
7  ProductB  quarter_3    300
8  ProductC  quarter_3    400
9  ProductA  quarter_4    250
10 ProductB  quarter_4    350
11 ProductC  quarter_4    450

```