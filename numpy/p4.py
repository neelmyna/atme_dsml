import numpy as np

array2 = np.full((3, 2), 5) 
print(array2)
print(array2[2][1]) # 5
print(array2[2][2]) # Error there is no 3rd row nor 3rd element
