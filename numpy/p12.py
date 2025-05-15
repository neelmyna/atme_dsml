import numpy as np

array = np.random.randint(1, 50, 3)
# Creates an numpy array of 3 elements between the range given
print(array)

array = np.random.randint(1, 3, 3)
# The range considered is [1, 3)
# It generates 'n' number of elements which is provided as 3rd argument
# Duplicate elements may be generated
# The generated elements need not be in order
# Creates a single list of integers
print(array)

array = np.random.randint(1, 100, 15)
print(array)
array2 = sorted(array)
print(array2)
print(type(array2))