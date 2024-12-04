'''
2. Do the following using PANDAS Series:
a. Create a series with 5 elements. Display the series sorted on index and also sorted on values seperately
b. Create a series with N elements with some duplicate values. Find the minimum and maximum ranks assigned to the values using ‘first’ and ‘max’ methods
c. Display the index value of the minimum and maximum element of a Series

'''

import pandas as pd

# Part (a)
series_a = pd.Series([15, 42, 8, 23, 4])
sorted_by_index = series_a.sort_index()
sorted_by_values = series_a.sort_values()
print("Original Series:\n", series_a)
print("Sorted by Index:\n", sorted_by_index)
print("Sorted by Values:\n", sorted_by_values)

# Part (b)
series_b = pd.Series([10, 20, 20, 30, 10, 40, 30, 40])
ranks_first = series_b.rank(method='first')
ranks_max = series_b.rank(method='max')
print("Original Series:\n", series_b)
print("Ranks (method='first'):\n", ranks_first)
print("Ranks (method='max'):\n", ranks_max)

# Part (c)
series_c = pd.Series([45, 67, 12, 89, 34])
min_index = series_c.idxmin()
max_index = series_c.idxmax()
print("Original Series:\n", series_c)
print("Index of Minimum Element:", min_index)
print("Index of Maximum Element:", max_index)
