string = input('Enter a string: ')
doubled = ''
for char in string:
    # repeat the character twice and concatenate to "doubled"
    doubled = doubled + char * 2

print(doubled)