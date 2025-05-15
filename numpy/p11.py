import numpy as np

arr = np.ones([3, 5])
print('arr: \n', arr)
print()
i = 1
for array in arr:
    # print(f'Row-{i} = {array}')
    # i += 1
    for element in array:
        print(element, end=', ')
    print()