#To initialize an Array/List of multi dimentional, with all elements Zero, we use the method zeroes()
import numpy as np

my_number = int(input('Enter a number of your choice: '))
array2 = np.full((1, 5), my_number) # Creates numpy array (ndarray) with a List of numbers where the value of the number is specified by the user.
print(array2)

print(array2[0]) # Prints the 1st list in the 2D list
print(array2[0][1]) # Prints the 2nd element in the 1st list
print(array2[1][0]) # Error. There is no 2nd list