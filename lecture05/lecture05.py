total_sales = 8000
num_employees = 6
TIP_PERCENT = 0.025

# total_tips = total_sales * TIP_PERCENT 
print('At a rate of', TIP_PERCENT * 100, '%')
tips_per_employee = total_sales * TIP_PERCENT / num_employees
print('Each employee takes home $', tips_per_employee)

# slide 9 - "bad example"
tips_per_employee = 8000 * 0.02 / 6
print('Each employee takes home $', tips_per_employee)

# slide 10 - magic number exceptions
TWO = 2 # doesn't make the meaning more clear
PI = 3.14159
# circumference = TWO * PI * radius

# slide 11 - input example
# lunch = 'tacos'
# print("Let's go get some", lunch)
# lunch = input('What would you like for lunch? ')
# drink = input('What would you like to drink? ')
# print("Let's go get some", lunch)
# print('and have a', drink)

# slide 17 - escape sequences
# print('One line
# second line') # SyntaxError
print('\n\n\n')
print('One line \ with backslash')
print('One line\nsecond line')
print('Stop 1\tStop 2')
print('Cat\tDog')
print('A long name\tDinosaur')
print('\tTab at the beginning')

# slide 18
print('What the @#$@!?')
# print('Ace of ♠')  
# print('Ace of \u2660')
print('This should be a dollar sign: \u0024')
print('Phi: Φ')