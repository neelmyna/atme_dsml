import list_operations as lo
import sys

choice = 0
stack = []

while True:
    choice = int(input(('1:Push 2:Pop 3:DisplayStack 4:Exit. Your choice please: ')))
    match(choice):
        case 1 : lo.insert_rear(stack)
        case 2 : lo.delete_rear(stack)
        case 3 : lo.display_from_rear(stack)
        case 4 : sys.exit('End of program')
        case _ : print('Invalid choice enetered')
