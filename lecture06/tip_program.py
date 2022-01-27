TIP_PERCENT = 0.025
total_sales = float(input('Enter the total sales: '))
num_employees = int(input('Enter the number of employees: '))

print(f'At a rate of {TIP_PERCENT:.1%}')
tips_per_employee = total_sales * TIP_PERCENT / num_employees
print(f'Each employee takes home ${tips_per_employee:.2f}')