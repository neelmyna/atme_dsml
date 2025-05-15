import numpy as np
a1 = np.array([4, 9, 11, 19, 27, 31, 38, 48, 63, 85, 89, 95, 105, 119])

print(np.mean(a1))
# mean is nothing but Average, which is the quotient of sum of the elements of the array divided by number of elements in the array.
print(type(np.mean(a1)))

print(np.median(a1))
# Meadian is the middle element of the sorted list/array of the original array.
# If Even number of elements is present in the array, then the 2 mid elements are added and their average is the median.

# The mean() and Median() always returns float64 (double) type value.

# A standard deviation (or σ) is a measure of how dispersed the data is in relation to the mean. Low standard deviation means data are clustered around the mean, and high standard deviation indicates data are more spread out.
# a quantity expressing by how much the members of a group differ from the mean value for the group
#
'''
sigma = population standard deviation
N	  =	the size of the population
ele   =	each value from the population
mu	  =	the population mean  (avg)
'''
# s_d = sq_root(sum(square(every_ele - mu)) / N)

a2 = np.array([300, 400, 350, 279, 480, 370])
print(np.std(a2))

a3 = np.array([180, 182, 185, 181, 182, 178])
print(np.std(a3))

a4 = np.array([165, 166, 165.7, 165.2, 166.15, 166.5])
print(np.std(a4))
