# Problem 1
TOTAL_ROPE = 10

branch_height = float(input('Enter the height of the tree branch: '))
rope_up_down = branch_height * 2
extra_rope = TOTAL_ROPE - rope_up_down
print(f'Amount of rope needed to go up then down: {rope_up_down:.1f} m')
print(f'Extra rope leftover: {extra_rope:.1f} m')

# Problem 2
SUGAR = 1.5
BUTTER = 1
FLOUR = 2.75
TOTAL_COOKIES = 48

n_cookies = int(input('How many cookies would you like to make? '))
scale = n_cookies / TOTAL_COOKIES
print('You will need:')
print(f'{SUGAR * scale:.2f} cups sugar')
print(f'{BUTTER * scale:.2f} cups butter')
print(f'{FLOUR * scale:.2f} cups flour')


print(f'{"sugar:":<8}{SUGAR * scale:>5.2g} cups')
print(f'{"butter:":<8}{BUTTER * scale:>5.2g} cups')
print(f'{"flour:":<8}{FLOUR * scale:>5.2g} cups')

# Problem 3
RATIO = 16 / 10

diag = float(input('Enter the diagonal size of the display (in inches): '))
height = (diag**2 / (1 + RATIO**2)) ** 0.5
width = RATIO * height
print(f'The height is {height:.1f}" and the width is {width:.1f}"')