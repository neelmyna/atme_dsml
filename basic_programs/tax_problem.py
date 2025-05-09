name = input('Enter employee name: ')
id = int(input('Enter employee Id: '))
monthly_basic_salary = float(input('Enter employee salary: '))
monthly_allowances = float(input('Enter Monthly allowance of the employee: '))
bonus_percentage = float(input('Enter the bonus percentage: '))

monthly_gross_salary = monthly_basic_salary + monthly_allowances
annual_bonus = (monthly_gross_salary * 12) * (bonus_percentage / 100)
annual_gross_salary = (monthly_gross_salary * 12) + annual_bonus

'''
print('Employee Id = ', id)
print('Employee Name = ', name)
print('Gross Monthly Salary = ', monthly_gross_salary)
print('Gross Annual Salary = ', annual_gross_salary)
'''

print('%-6s %-15s %7s %-15s %s '%('ID', 'NAME', 'BONUS', 'MONTHLY_SALARY', 'ANNUAL_SALARY'))
print('-' * 70)
print('%-6d %-15s %6.2f%% %15.2f %.2f'%(id, name, bonus_percentage, monthly_gross_salary, annual_gross_salary))