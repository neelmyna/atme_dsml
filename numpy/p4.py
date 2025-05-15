import numpy as np

array2 = np.full((3, 2), 5) 
print(array2)
print(array2[2][1]) # 5
print(array2[4][1]) # Error there is no 3rd `column`
