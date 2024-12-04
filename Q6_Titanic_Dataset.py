'''Using Titanic dataset, to do the following:
a. Clean the data by dropping the column which has the largest number of missing values. b. Find total number of passengers with age more than 30
c. Find total fare paid by passengers of second class d. Compare number of survivors of each passenger class
e. Compute descriptive statistics for age attribute gender wise
f. Draw a scatter plot for passenger fare paid by Female and Male passengers separately
g. Compare density distribution for features age and passenger fare
h. Draw the pie chart for three groups labelled as class 1, class 2, class 3 respectively displayed in different colours. The occurrence of each group converted into percentage should be displayed in the pie chart. Appropriately Label the chart.
i. Find % of survived passengers for each class and answer the question “Did class play a role in survival?”.
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Titanic dataset
df = pd.read_csv('titanic.csv')  # Replace with the correct path to the dataset

# Part (a): Clean the data by dropping the column which has the largest number of missing values
col_with_max_missing = df.isnull().sum().idxmax()
df_cleaned = df.drop(columns=[col_with_max_missing])
print(f"Dropped column: {col_with_max_missing}")

# Part (b): Find total number of passengers with age more than 30
age_above_30 = df[df['Age'] > 30].shape[0]
print(f"Total passengers with age more than 30: {age_above_30}")

# Part (c): Find total fare paid by passengers of second class
total_fare_second_class = df[df['Pclass'] == 2]['Fare'].sum()
print(f"Total fare paid by second class passengers: {total_fare_second_class}")

# Part (d): Compare number of survivors of each passenger class
survivors_by_class = df.groupby('Pclass')['Survived'].sum()
print("Number of survivors by class:\n", survivors_by_class)

# Part (e): Compute descriptive statistics for age attribute gender-wise
age_stats_gender = df.groupby('Sex')['Age'].describe()
print("Descriptive statistics for age attribute gender-wise:\n", age_stats_gender)

# Part (f): Draw a scatter plot for passenger fare paid by Female and Male passengers separately
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Fare', y='Age', data=df[df['Sex'] == 'female'], color='blue', label='Female')
sns.scatterplot(x='Fare', y='Age', data=df[df['Sex'] == 'male'], color='red', label='Male')
plt.title('Passenger Fare vs Age by Gender')
plt.xlabel('Fare')
plt.ylabel('Age')
plt.legend()
plt.show()

# Part (g): Compare density distribution for features age and passenger fare
plt.figure(figsize=(8, 6))
sns.kdeplot(df['Age'].dropna(), shade=True, label='Age', color='blue')
sns.kdeplot(df['Fare'].dropna(), shade=True, label='Fare', color='green')
plt.title('Density Distribution of Age and Fare')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()

# Part (h): Draw the pie chart for three groups labelled as class 1, class 2, class 3 respectively displayed in different colours
class_counts = df['Pclass'].value_counts()
class_percentage = class_counts / class_counts.sum() * 100
colors = ['gold', 'lightblue', 'lightgreen']
plt.figure(figsize=(8, 6))
plt.pie(class_percentage, labels=['Class 1', 'Class 2', 'Class 3'], colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Passenger Class Distribution')
plt.show()

# Part (i): Find % of survived passengers for each class and answer the question “Did class play a role in survival?”
survival_rate_by_class = df.groupby('Pclass')['Survived'].mean() * 100
print("Survival rate by class (%):\n", survival_rate_by_class)
