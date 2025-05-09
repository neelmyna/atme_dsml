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

