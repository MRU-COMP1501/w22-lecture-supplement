# reads and parses a list of numbers from a user
def parse_input(input_str):
    num_list = []
    for num_str in input_str.split():
        num_list.append(float(num_str))
    return num_list

def main():
    list_str = input('Enter a list of numbers: ')
    nums = parse_input(list_str)
    print(nums)
    print(type(nums))

main()