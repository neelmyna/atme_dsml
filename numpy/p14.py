import numpy as np
#hstack()

a1 = np.array([2, 4])
a2 = np.array([300, 9119, 7, 5])
a3 = np.array([0, 101, 323])
a4 = np.ones([3, 5])
a5 = np.ones([3, 4])

# hstack() 'h' stands for horizontal
# Unlike vstack, hstack() can stack arrays of different sizes.
# The output the method hstack() returns is always 1D array
# When we apply hstack() on 2D arrays as the i/p then the number of rows must be same. The column numbers may differ.
print(np.hstack((a1, a2)))
print(np.hstack((a1, a2, a3)))
print(np.hstack((a4, a5)))
#print(np.hstack((a1, a2, a3, a4))) #Error a4 is f differenbt dimension