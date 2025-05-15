'''
To Create numpy array/list with a range of values:
Method is arange()
It takes 2 arguments or 3 arguments
arange(1, 10) # The range is from 1 to 9. Note that the 2nd Arg is excluded.
arange(1, 20, 3) # The 3rd Arg depicts the increment for every element in the List

Note: arange() create a 1D List and not 2D list
'''
import numpy

arr3 = numpy.arange(1, 10)  # [1, 10)
arr4 = numpy.arange(1, 20, 4)
print(f'Arr3 = {arr3}')
print(f'Arr4 = {arr4}')
print(f'Type of Arr3 = {type(arr3)}')
