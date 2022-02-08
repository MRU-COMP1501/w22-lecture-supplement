# Note: this does not work on Windows!
input_str = input('Enter numbers to sum together: ')
num_sum = 0
for num in input_str:
    # convert the number to an integer and add to sum
    print(num)
    num_sum += int(num)

print(num_sum)