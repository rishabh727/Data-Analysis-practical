'''
Consider the following data frame containing a family name, gender of the family member and her/his monthly income in each record.
FamilyName Gender MonthlyIncome (Rs.)
Shah Male 44000.00
Vats Male 65000.00
Vats Female 43150.00
Kumar Female 66500.00
Vats Female 255000.00
Kumar Male 103000.00
Shah Male 55000.00
Shah Female 112400.00
Kumar Female 81030.00
Vats Male 71900.00
Write a program in Python using Pandas to perform the following:
a. Calculate and display familywise gross monthly income.
b. Display the highest and lowest monthly income for each family name
c. Calculate and display monthly income of all members earning income less than Rs. 80000.00.
d. Display total number of females along with their average monthly income
e. Delete rows with Monthly income less than the average income of all members

'''
import pandas as pd

# Create the data frame
data = {
    "FamilyName": ["Shah", "Vats", "Vats", "Kumar", "Vats", "Kumar", "Shah", "Shah", "Kumar", "Vats"],
    "Gender": ["Male", "Male", "Female", "Female", "Female", "Male", "Male", "Female", "Female", "Male"],
    "MonthlyIncome (Rs.)": [44000.00, 65000.00, 43150.00, 66500.00, 255000.00, 103000.00, 55000.00, 112400.00, 81030.00, 71900.00]
}
df = pd.DataFrame(data)

# Part (a): Calculate and display familywise gross monthly income
familywise_income = df.groupby("FamilyName")["MonthlyIncome (Rs.)"].sum()
print("Familywise Gross Monthly Income:\n", familywise_income)

# Part (b): Display the highest and lowest monthly income for each family name
highest_income = df.groupby("FamilyName")["MonthlyIncome (Rs.)"].max()
lowest_income = df.groupby("FamilyName")["MonthlyIncome (Rs.)"].min()
print("\nHighest Monthly Income for Each Family:\n", highest_income)
print("\nLowest Monthly Income for Each Family:\n", lowest_income)

# Part (c): Calculate and display monthly income of all members earning less than Rs. 80000.00
below_80k = df[df["MonthlyIncome (Rs.)"] < 80000.00]
print("\nMonthly Income of Members Earning Less Than Rs. 80000.00:\n", below_80k)

# Part (d): Display total number of females along with their average monthly income
female_stats = df[df["Gender"] == "Female"]
total_females = female_stats.shape[0]
average_female_income = female_stats["MonthlyIncome (Rs.)"].mean()
print("\nTotal Number of Females:", total_females)
print("Average Monthly Income of Females:", average_female_income)

# Part (e): Delete rows with monthly income less than the average income of all members
average_income = df["MonthlyIncome (Rs.)"].mean()
df_filtered = df[df["MonthlyIncome (Rs.)"] >= average_income]
print("\nData Frame After Removing Rows with Monthly Income Less Than Average Income:\n", df_filtered)
