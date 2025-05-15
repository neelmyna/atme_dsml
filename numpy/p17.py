import numpy as np
a1 = np.array([2, 4, 9, 19, 7, 11])
a2 = np.array([23, 4, 9, 15, 11, 20])
# Intersection of 2 arrays (set of values)

a3 = np.array([[2, 4, 6, 7, 9, 8], [12, 21, 20, 15, 18, 18]])
arr = np.array([a1, a2])
print(arr)
a4 = np.array([[3, 4, 9, 4, 1, 8], [12, 22, 21, 17, 13, 18]])

#a5 = np.array([[2, 4, 6], [7, 9, 8], [12, 21, 20], [15, 18, 20]])
#a6 = np.array([[3, 4, 9], [2, 4, 6], [12, 21, 20], [17, 13, 20]])

#a7 = np.array([[2, 4, 6], [7, 9, 8], [12, 21, 20], [15, 18, 20], [1, 2, 3]])
#a8 = np.array([[3, 4, 9], [2, 4, 6], [12, 21, 20], [17, 13, 20], [1, 2, 3]])

print(np.intersect1d(a1, a2))
print(np.intersect1d(a3, a4))
#print(np.intersect1d(a5, a6))
#print(np.intersect1d(a7, a8))

#for i in range(len(a3)):
#	print(np.intersect1d(a3[i], a4[i]))

# The intersect1d() returns an ORDERED SET (list or array of UNIQUE elements of 1 dimention only)
# Even if we are intersecting arrays of 2D, the intersect1d() returns a 1D list of intersecting unique elements.
# The list of intersecting unique elements returned by intersect1d() is always ordered.
# If there are no common elements between the i/p lists, then intersect1d() returns an empty set