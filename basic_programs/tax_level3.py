name = input('Enter employee name: ')
id = int(input('Enter employee Id: '))
monthly_basic_salary = float(input('Enter employee salary: '))
monthly_allowances = float(input('Enter Monthly allowance of the employee: '))
bonus_percentage = float(input('Enter the bonus percentage: '))

monthly_gross_salary = monthly_basic_salary + monthly_allowances
annual_bonus = (monthly_gross_salary * 12) * (bonus_percentage / 100)
annual_gross_salary = (monthly_gross_salary * 12) + annual_bonus

standard_deduction = 50000
taxable_salary = annual_gross_salary - standard_deduction
print(f'Taxable Annual Salary = {taxable_salary}')

print('-' * 27)
print('%12s %s'%('Salary_Range', 'Tax_Percentage'))
print('-' * 27)
print('%-12d %-d'%(0, 300000))
print('%-12d %-d'%(300001, 600000))
print('%-12d %-d'%(600000, 900000))
print('%-12d %-d'%(900000, 1200000))
print('%-12d %-d'%(1200000, 1500000))
print('%-12d %-d'%(150000))