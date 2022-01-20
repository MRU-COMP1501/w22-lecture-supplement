# inputs: pennies
# outputs: dollars, cents
# approach 1: 
# calculate dollars as pennies / 100 rounded down
# calculate cents as remainder of previous operation
# display dollars and cents

pennies = 1729
dollars = pennies // 100
cents = pennies % 100
print(dollars, 'dollars and', cents, 'cents')

# alternative solution
dollars = int(pennies / 100)
cents = pennies - dollars*100
print(dollars, 'dollars and', cents, 'cents')
