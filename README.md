# pandas-learning
pandas-learning

Panda things to learn:
1. How to create DataFrames
- What shape must the raw data model be in
- How can the raw data model be put into a DataFrame

- Looks like the data model can either be a list of lists or a dict of lists
  - If it's a list of lists, each sub-list must have the same shape,
  - and the DataFrame constructor needs the list data as an argument and a column key argument specifying the column names
  - If it's a dict of lists, the dict can be put into the DataFrame constructor without specifying column names (the keys are column names)

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

2. How to read DataFrames

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