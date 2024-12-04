'''
Consider two excel files having attendance of two workshops, each of duration 5 days. Each file has three fields ‘Name’, ‘Date, duration (in minutes) where names may be repetitve within a file. Note that duration may take one of three values (30, 40, 50) only. Import the data into two data frames and do the following:
a. Perform merging of the two data frames to find the names of students who had attended both workshops.
b. Find names of all students who have attended a single workshop only.
c. Merge two data frames row-wise and find the total number of records in the data frame.
d. Merge two data frames row-wise and use two columns viz. names and dates as multi-row indexes. Generate descriptive statistics for this hierarchical data frame.
'''

import pandas as pd

# Import the data from two Excel files
df1 = pd.read_excel('workshop1.xlsx')
df2 = pd.read_excel('workshop2.xlsx')

# Part (a): Perform merging of the two data frames to find the names of students who had attended both workshops
common_students = pd.merge(df1, df2, on='Name', how='inner')
print("Students who attended both workshops:\n", common_students['Name'].unique())

# Part (b): Find names of all students who have attended a single workshop only
all_names = pd.concat([df1['Name'], df2['Name']]).drop_duplicates()
single_workshop = all_names[~all_names.isin(common_students['Name'])]
print("Students who attended only one workshop:\n", single_workshop)

# Part (c): Merge two data frames row-wise and find the total number of records in the data frame
merged_rowwise = pd.concat([df1, df2], ignore_index=True)
total_records = len(merged_rowwise)
print("Total number of records after row-wise merge:", total_records)

# Part (d): Merge two data frames row-wise and use two columns (names and dates) as multi-row indexes
hierarchical_df = merged_rowwise.set_index(['Name', 'Date'])
descriptive_stats = hierarchical_df.describe()
print("Descriptive Statistics for Hierarchical Data Frame:\n", descriptive_stats)

