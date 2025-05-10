# Program to print X shape of N lines where N is Odd number.
'''
*

**
**

* *
 *
* *

*  *
 **
 **
*  *

*   *
 * *
  *
 * *
*   *

*    *
 *  *
  **
  **
 *  *
*    *
'''
import pdb
pdb.set_trace()

number_of_lines = int(input('Enter number of lines of X: '))

for row_number in range(number_of_lines):
    for column_number in range(number_of_lines):
        if row_number == column_number or column_number+1 == number_of_lines - row_number:
            print('* ', end='')
        else:
            print('  ', end='')
    print()

