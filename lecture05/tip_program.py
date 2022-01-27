TIP_PERCENT = 0.025
total_sales = float(input('Enter the total sales: '))
num_employees = int(input('Enter the number of employees: '))

print('At a rate of', TIP_PERCENT * 100, '%')
tips_per_employee = total_sales * TIP_PERCENT / num_employees
print('Each employee takes home $', tips_per_employee)