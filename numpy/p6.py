import numpy

arr5 = numpy.full(1, 5) # 1D Array of 1 element which is 5
print(f'Arr5 = {arr5}')

arr6 = numpy.full((1, 5)) # Error
print(f'Arr6 = {arr6}')

arr7 = numpy.full((1, 5), 5) # 1D Array of 5 elements each of whose value is 5
print(f'Arr7 = {arr7}')