input_str = input('Enter a string: ')
# input_str = input_str.upper() # make it uppercase
for c in input_str:
    upper_c = c.upper()
    print(f'Give me a {c}: {upper_c}!')
    c = upper_c

print('c:', c)
print('input_str:', input_str)
print('What does that spell? ' + input_str.upper())