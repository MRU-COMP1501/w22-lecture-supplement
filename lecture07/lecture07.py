import math
from math import sqrt
from random import randint

# slide 7 - line break example with strings
print(f'A really long f-string that has some {1234} numbers in it and maybe some other things A really long f-string that has some {1234} numbers in it and maybe some other things')
print(f'A really long f-string that has '
      f'some {1234} numbers in it and '
      f'maybe some other things'
      f'A really long f-string that has '
      f'some {1234} numbers in it and '
      f'maybe some other things')

# multiple variables in a single f-string
x = 5
y = 6
z = 7
print(f'x = {x}, y = {y}, z = {z:.1f}')

# slide 11 - string methods
print('\n\n')
hello = 'hello world'
print(hello.capitalize())
print(hello.upper())

# float methods - not very many
x = 0.25
print(x.as_integer_ratio())

# slide 17
print('\n\n')
print('Slide 17')
shout_hello = hello.upper()
print(shout_hello * 3)

# slide 18
print_return = print(shout_hello)
print(print_return) # prints None

# slide 19
# Ctrl + / to comment/uncomment
# print('Nested Function calls: ', print(len('Hello')))
print('Nested Function calls: ', len('Hello'))

# slide 20
print('\n\nSlide 20')
print(f'The square root of 1024 is: {sqrt(1024)}')
print(f'cos(180 degrees) is: {math.cos(math.radians(180))}')

# slide 21
print('\n\nSlide 21')
roll = randint(1, 6)
print(f'You rolled a {roll}')