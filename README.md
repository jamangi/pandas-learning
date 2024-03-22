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
```

list of lists:
```py
import pandas as pd
data = [[1, 'Wang', 'Allen'], [2, 'Alice', 'Bob']]
person = pd.DataFrame(data, columns=['personId', 'firstName', 'lastName']).astype({'personId':'Int64', 'firstName':'object', 'lastName':'object'})
data = [[1, 2, 'New York City', 'New York'], [2, 3, 'Leetcode', 'California']]
address = pd.DataFrame(data, columns=['addressId', 'personId', 'city', 'state']).astype({'addressId':'Int64', 'personId':'Int64', 'city':'object', 'state':'object'})
```