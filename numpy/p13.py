# VStack
# vstack()  V means Verticle. This is to place one array upon another
# vstack() takes one Arg. Thus the arrays we pass must be placed inside paranthesis
# The number of elements in all the arrays must be same
# vstack() can Stack multiple arrays
# Thus we use vStack to convert N number of 1D arrays into a 2D Array
# Note: The size of all the arrays we wish to stack must be of the same size
import numpy as np

a1 = np.array([22, 42, 6, 81])
a2 = np.array([30, 91, 7, 51])
a3 = np.array([0, 10, 23, 32])

print(np.vstack( (a1, a2, a3) )) # place a1 on a2 and a2 on a3
print('\n')
print(np.vstack((a3, a1, a2, a1)))

a4 = np.ones([3, 5])
a5 = np.ones([3, 5])

v_array = np.vstack((a4, a5))
print(v_array)