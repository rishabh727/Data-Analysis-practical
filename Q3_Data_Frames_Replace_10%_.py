'''
Create a data frame having at least 3 columns and 50 rows to store numeric data generated using a random function. Replace 10% of the values by null values whose index positions are generated using random function. Do the following:
a. Identify and count missing values in a data frame.
b. Drop the column having more than 5 null values.
c. Identify the row label having maximum of the sum of all values in a row and drop that row.
d. Sort the data frame on the basis of the first column.
e. Remove all duplicates from the first column.
f. Find the correlation between first and second column and covariance between second and third column.
g. Discretize the second column and create 5 bins.

'''
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(50, 3), columns=['Col1', 'Col2', 'Col3'])
num_nulls = int(0.1 * df.size)
null_indices = np.random.choice(df.size, size=num_nulls, replace=False)
df.values.ravel()[null_indices] = np.nan

# Part (a): Identify and count missing values
missing_count = df.isnull().sum().sum()
print("Total Missing Values:", missing_count)

# Part (b): Drop the column having more than 5 null values
columns_to_drop = df.columns[df.isnull().sum() > 5]
df = df.drop(columns=columns_to_drop, axis=1)

# Part (c): Identify the row label having maximum of the sum of all values in a row and drop that row
row_with_max_sum = df.sum(axis=1).idxmax()
df = df.drop(row_with_max_sum, axis=0)

# Part (d): Sort the data frame on the basis of the first column
df = df.sort_values(by='Col1')

# Part (e): Remove all duplicates from the first column
df = df.drop_duplicates(subset='Col1')

# Part (f): Find the correlation between first and second column and covariance between second and third column
correlation = df['Col1'].corr(df['Col2'])
covariance = df['Col2'].cov(df['Col3'])
print("Correlation between Col1 and Col2:", correlation)
print("Covariance between Col2 and Col3:", covariance)

# Part (g): Discretize the second column and create 5 bins
df['Col2_Binned'] = pd.cut(df['Col2'], bins=5)
print("Data Frame with Binned Column:\n", df)
