import numpy
# full() It takes 2 Args. If the 1st Arg is a number, then 1D array is created with the 1st Arg as number of values in the 1D array and the 2nd Arg as the value.
# If the 1st Arg is a tuple, then as usual, the 1st value in the tuple is the number of rows and the 2nd value in the tuple would be the numbers of columns.

arr5 = numpy.full(1, 5) # 1D Array of 1 element which is 5
print(f'Arr5 = {arr5}')

arr6 = numpy.full( (1, 5) ) # full method takes 2 Args
print(f'Arr6 = {arr6}')

arr7 = numpy.full( (1, 5), 50) # 1D Array of 5 elements each of whose value is 50
print(f'Arr7 = {arr7}')

arr8 = numpy.full(5, 1) # 1D Array of 5 elements which is 1
print(f'Arr8 = {arr8}')