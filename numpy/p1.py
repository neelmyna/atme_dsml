import numpy as np

array = np.array([[1, 3.3, 4.4, 4, 4, 5, 7, 12]])
print('Array: \n', array)
print('Type of Array =', type(array))
print('Array[0]: \n', array[0])
print('Type of Array[0] =', type(array[0]))
print('Array[0][0]: \n', array[0][0])
print('Type of Array[0][0]: \n', type(array[0][0]))

print('Array[1]: \n', array[1]) # error. There is no 2nd 1D array in the 2D array
print('Type of Array[1] =', type(array[1]))
