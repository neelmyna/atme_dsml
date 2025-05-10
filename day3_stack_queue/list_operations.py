def insert_rear(array):
    data = input('Enter the data to be inserted at rear: ')
    array.append(data)

def insert_front(array):
    data = input('Enter the data to be inserted at front: ')
    array.insert(0, data)

def delete_rear(array):
    if len(array) == 0:
        print('Array is empty')
        return
    deleted_data = array.pop()
    print(f'Delete element is {deleted_data}')
       
def delete_front(array):
    if len(array) == 0:
        print('Array is empty')
        return
    deleted_data = array[0]
    del array[0]
    print(f'Delete element is {deleted_data}')

def display_from_rear(array):
    if len(array) == 0:
        print('Array is empty')
        return
    print(array[::-1])

def display_from_front(array):
    if len(array) == 0:
        print('Array is empty')
        return
    print(array) # print(array[:]) array[::]