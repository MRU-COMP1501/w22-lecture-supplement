import math

a = 5
b = 4
c = math.sqrt(9 * (a - b)) # a - b = 1, c = 3
c = round(c) # c = 3
drink = input('What would you like to drink? ') + ' ' # drink = user input
print('You chose: ' + drink.upper() * c)
# prints 'You chose: DRINK DRINK DRINK'