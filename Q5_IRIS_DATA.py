'''
Using Iris data, plot the following with proper legend and axis labels: (Download IRIS data from: https://archive.ics.uci.edu/ml/datasets/iris or import it from sklearn datasets)
a. Load data into pandas’ data frame. Use pandas.info () method to look at the info on datatypes in the dataset.
b. Find the number of missing values in each column (Check number of null values in a column using df.isnull().sum())
c. Plot bar chart to show the frequency of each class label in the data.
d. Draw a scatter plot for Petal Length vs Sepal Length and fit a regression line
e. Plot density distribution for feature Petal width.
f. Use a pair plot to show pairwise bivariate distribution in the Iris Dataset.
g. Draw heatmap for any two numeric attributes
h. Compute mean, mode, median, standard deviation, confidence interval and standard error for each numeric feature
i. Compute correlation coefficients between each pair of features and plot heatmap

'''

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from scipy import stats

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['Species'] = iris.target
df['Species'] = df['Species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Part (a): Load data into pandas DataFrame and check info
print(df.info())

# Part (b): Find the number of missing values in each column
missing_values = df.isnull().sum()
print("Missing values in each column:\n", missing_values)

# Part (c): Plot bar chart to show the frequency of each class label
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Species', palette='Set2')
plt.title('Frequency of Each Class Label')
plt.xlabel('Species')
plt.ylabel('Frequency')
plt.show()

# Part (d): Draw scatter plot for Petal Length vs Sepal Length and fit a regression line
plt.figure(figsize=(8, 6))
sns.regplot(x='petal length (cm)', y='sepal length (cm)', data=df, scatter_kws={'color': 'blue'}, line_kws={'color': 'red'})
plt.title('Petal Length vs Sepal Length with Regression Line')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Sepal Length (cm)')
plt.show()

# Part (e): Plot density distribution for feature Petal Width
plt.figure(figsize=(8, 6))
sns.kdeplot(df['petal width (cm)'], shade=True, color='green')
plt.title('Density Distribution of Petal Width')
plt.xlabel('Petal Width (cm)')
plt.ylabel('Density')
plt.show()

# Part (f): Use a pair plot to show pairwise bivariate distribution
sns.pairplot(df, hue='Species', palette='Set1')
plt.suptitle('Pairwise Bivariate Distribution in Iris Dataset', y=1.02)
plt.show()

# Part (g): Draw heatmap for any two numeric attributes
corr_matrix = df[['sepal length (cm)', 'petal length (cm)']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Heatmap for Sepal Length and Petal Length')
plt.show()

# Part (h): Compute mean, mode, median, standard deviation, confidence interval, and standard error for each numeric feature
numeric_features = df[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']]

mean = numeric_features.mean()
mode = numeric_features.mode().iloc[0]
median = numeric_features.median()
std_dev = numeric_features.std()
conf_interval = stats.t.interval(0.95, len(numeric_features) - 1, loc=mean, scale=std_dev / np.sqrt(len(numeric_features)))
std_error = numeric_features.sem()

print("Mean:\n", mean)
print("Mode:\n", mode)
print("Median:\n", median)
print("Standard Deviation:\n", std_dev)
print("Confidence Interval:\n", conf_interval)
print("Standard Error:\n", std_error)

# Part (i): Compute correlation coefficients between each pair of features and plot heatmap
corr_matrix_full = numeric_features.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix_full, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Features')
plt.show()

