import numpy as np
#column_stack()

a1 = np.array([2, 4, 9])
a2 = np.array([300, 7, 5])
a3 = np.array([0, 101, 323])

# column_stack() 
# The elements from the numpy arrays, column wise are taken and a row is created.
#Note that the number of elements in the i/p arrays must be same.
print(np.column_stack((a1, a2)))
print(np.column_stack((a1, a2, a3)))