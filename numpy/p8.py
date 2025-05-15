import numpy as np

arr = np.arange(1, 10)
print(arr, '\n') # 1D Array of elements from 1 to 9

# Reshape to 3x3 matrix
arr = arr.reshape(3, 3)
print(arr, '\n')

# Reshape back to the original size
arr = arr.reshape(9) # creates 1D array
print(arr)

arr = arr.reshape(9, 1)
print(arr)

arr = arr.reshape(1, 9) # Creates 2D array
print(arr)