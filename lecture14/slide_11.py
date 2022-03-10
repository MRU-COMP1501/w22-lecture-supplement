def with_guard(word):
    if len(word) != 5:
        print('Words must be exactly 5 letters')
        return None

def with_nesting(word):
    if len(word) == 5:
        # do the rest of the function
        pass
    else:
        print('Words must be exactly 5 letters')
        return None

if __name__ == '__main__':
    with_guard('not five')
    with_nesting('not five')
    