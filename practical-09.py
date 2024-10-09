# ARRAY CREATION

# Program to create a 1D and 2D array using NumPy
import numpy as np

# Creating a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

# Creating a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)

# ================================
# ARRAY SHAPE & SIZE

# Program to find shape and size of a NumPy array

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Getting the shape of the array
print("Shape of array:", array.shape)

# Getting the size (number of elements)
print("Size of array:", array.size)
# ================================
# ARRAY SLICING

# Program to slice a NumPy array

array = np.array([10, 20, 30, 40, 50])

# Slicing the array to get elements from index 1 to 3
sliced_array = array[1:4]
print("Sliced Array:", sliced_array)
# ================================
# ARRAY RESHAPING

# Program to reshape a NumPy array

array = np.array([1, 2, 3, 4, 5, 6])

# Reshaping into a 2x3 array
reshaped_array = array.reshape(2, 3)
print("Reshaped Array:\n", reshaped_array)
# ================================
# ARRAY ARITHMETIC OPERATIONS

# Program for arithmetic operations on NumPy arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Element-wise addition
addition = array1 + array2
print("Addition:", addition)

# Element-wise multiplication
multiplication = array1 * array2
print("Multiplication:", multiplication)
# ================================
# ARRAY BROADCASTING

# Program to demonstrate broadcasting in NumPy

array = np.array([1, 2, 3])

# Broadcasting a scalar value
broadcasted_array = array + 10
print("Broadcasted Array:", broadcasted_array)