def lowest_3(nums):
    # option 1
    # nums_copy = nums.copy()
    # nums_copy.sort() # modifies nums_copy in place
    # return nums_copy[:3]

    # option 2
    sorted_nums = sorted(nums)
    return sorted_nums[:3]

def main():
    some_nums = [1,2,3,4,6,9,1,2,0,3,1]
    print(some_nums)
    print(lowest_3(some_nums))
    print(some_nums)

if __name__ == '__main__':
    main()