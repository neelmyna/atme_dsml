'''
Array shape
All arrays have a shape accessible using .shape
For example, let's get the shape of a vector, matrix, and tensor.
'''
import numpy as np

vector = np.arange(5)
print('Vector:', vector)
print("Vector shape:", vector.shape)

matrix = np.ones((3, 2))
print('Matrix:', matrix)
print('Matrix shape:', matrix.shape)

tensor = np.zeros((2, 3, 3))
print('Tensor:', tensor)
print('Tensor shape:', tensor.shape)

print(tensor[0][1][1]) #Prints the 1st Matrix's 2nd Row, 2nd element