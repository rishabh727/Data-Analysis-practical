'''Q1.
Write programs in Python using NumPy library to do the following:
a.	Create a two-dimensional array, ARR1 having random values from 0 to 1. Compute the mean, standard deviation, and variance of ARR1 along the second axis.

b.	Create a 2-dimensional array of size m x n integer elements, also print the shape, type and data type of
the array and then reshape it into an n x m array, where n and m are user inputs given at the run time.

c.	Test whether the elements of a given 1D array are zero, non-zero and NaN. Record the indices of these
elements in three separate arrays.

d.	Create three random arrays of the same size: Array1, Array2 and Array3. Subtract Array 2 from Array3
and store in Array4. Create another array Array5 having two times the values in Array1. Find Co-
variance and Correlation of Array1 with Array4 and Array5 respectively.

e.	Create two random arrays of the same size 10: Array1, and Array2. Find the sum of the first half of both
the arrays and product of the second half of both the arrays.

f.	g. Create an array with random values. Determine the size of the memory occupied by the array.
Create a 2-dimensional array of size m x n having integer elements in the range (10,100).
Write
statements to swap any two rows, reverse a specified column and store updated array in another
variable

'''
# PART A
import numpy as np

ARR1 = np.random.rand(5, 4) 
mean = np.mean(ARR1, axis=1)
std_dev = np.std(ARR1, axis=1)
variance = np.var(ARR1, axis=1)

print("Array ARR1:\n", ARR1)
print("Mean along the second axis:", mean)
print("Standard Deviation along the second axis:", std_dev)
print("Variance along the second axis:", variance)


#PART B

m = int(input("Enter the number of rows (m): "))
n = int(input("Enter the number of columns (n): "))


array = np.random.randint(1, 100, size=(m, n))


print("Original Array:\n", array)
print("Shape:", array.shape)
print("Type:", type(array))
print("Data Type:", array.dtype)


reshaped_array = array.reshape(n, m)
print("Reshaped Array:\n", reshaped_array)

#PART C

array = np.array([0, 1, np.nan, 2, 0, np.nan, 3])


zero_indices = np.where(array == 0)[0]
non_zero_indices = np.where(array != 0)[0]
nan_indices = np.where(np.isnan(array))[0]

print("Original Array:", array)
print("Indices of zero elements:", zero_indices)
print("Indices of non-zero elements:", non_zero_indices)
print("Indices of NaN elements:", nan_indices)

#PART D

size = 5
Array1 = np.random.rand(size)
Array2 = np.random.rand(size)
Array3 = np.random.rand(size)


Array4 = Array3 - Array2
Array5 = 2 * Array1


cov = np.cov(Array1, Array4)[0, 1]
corr = np.corrcoef(Array1, Array5)[0, 1]

print("Array1:", Array1)
print("Array2:", Array2)
print("Array3:", Array3)
print("Array4 (Array3 - Array2):", Array4)
print("Array5 (2 * Array1):", Array5)
print("Covariance (Array1 & Array4):", cov)
print("Correlation (Array1 & Array5):", corr)

#PART E

Array1 = np.random.rand(10)
Array2 = np.random.rand(10)


sum_first_half = np.sum(Array1[:5]) + np.sum(Array2[:5])
product_second_half = np.prod(Array1[5:]) * np.prod(Array2[5:])

print("Array1:", Array1)
print("Array2:", Array2)
print("Sum of first half of both arrays:", sum_first_half)
print("Product of second half of both arrays:", product_second_half)

#PART F

random_array = np.random.rand(100)

memory_size = random_array.nbytes
print("Array:", random_array)
print("Memory occupied by array (in bytes):", memory_size)

#PART G
m = int(input("Enter the number of rows (m): "))
n = int(input("Enter the number of columns (n): "))

array = np.random.randint(10, 100, size=(m, n))

row1, row2 = 0, 1  
array[[row1, row2]] = array[[row2, row1]]

column_to_reverse = 2  
array[:, column_to_reverse] = array[:, column_to_reverse][::-1]

updated_array = array.copy()

print("Original Array:\n", array)
print("Updated Array after row swap and column reverse:\n", updated_array)

