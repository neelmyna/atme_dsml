# Command Line Args

import sys
print(sys.argv)
print(sys.argv[0])
#print(sys.argv[2]) # IndexError if you given less than 10 elements

numbers = [int(number) for number in sys.argv[1:]]

print(numbers)
print(type(numbers))
print(numbers[1])
print(type(numbers[1]))