def square_list(nums):
    result = []
    try:
        for num in nums:
            result.append(num ** 2)
    except Exception as err:
        print(err)
        pass
    return result

def double_list(nums):
    result = []
    for num in nums:
        result.append(num * 2)
    return result

# print(square_list(['0','1','2']))
print(double_list(['0','1','2']))