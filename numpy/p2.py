import numpy as np
arr1 = np.zeros((1, 3)) # Created an Array of 1D (i.e. a single array) of 3 elements, all of which are zeroes. The Array created is nothing but a Python List.
print(arr1)
arr2 = np.zeros((2, 5))
print(arr2)
print(type(arr2))
print(arr2[0], '    ', type(arr2[0]))
print(arr2[0][0], '     ', type(arr2[0][0]))