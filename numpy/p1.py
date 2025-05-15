import numpy as np

array = np.array([[1, 1, 3, 3, 4, 4, 4, 5, 7, 7, 8, 9, 12]])
print(array)
mean   = np.mean(array)
median = np.median(array)
print(f'Mean = {mean}')
print(f'Median = {median}')