def count_pairs(some_nums):
    n_pairs = 0
    for i in range(1, len(some_nums)):
        if some_nums[i - 1] == 0 and some_nums[i] == 0:
            n_pairs += 1
    return n_pairs

if __name__ == '__main__':
    pairs = count_pairs([1, 2, 0, 0, 3, 4, 0, 0, 1, 0, 2, 5, 0, 8])
    print(f'Pairs of zeros: {pairs}')