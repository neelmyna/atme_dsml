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
print('Education and Health Cess = 4%')

cess = taxable_salary * 0.04
tax_amount = 0
if taxable_salary >= 0 and taxable_salary <= 300000:
    tax_amount = 0
elif taxable_salary >= 300001 and taxable_salary <= 600000:
    tax_amount = taxable_salary * 0.05
elif taxable_salary >= 300001 and taxable_salary <= 600000:
    tax_amount = taxable_salary * 0.05
elif taxable_salary >= 600001 and taxable_salary <= 900000:
    tax_amount = taxable_salary * 0.1
elif taxable_salary >= 900001 and taxable_salary <= 1200000:
    tax_amount = taxable_salary * 0.15
elif taxable_salary >= 1200001 and taxable_salary <= 1500000:
    tax_amount = taxable_salary * 0.2
elif taxable_salary >= 1500001:
    tax_amount = taxable_salary * 0.3

section_87a = int(input('Are you exempted under Section-87A. If Yes, press 1 else 0'))

if taxable_salary <= 700000 and section_87a == 1:
    tax_amount = 0

total_tax_payable = cess + tax_amount
print(f'Your Total Tax payable amount is {total_tax_payable}')