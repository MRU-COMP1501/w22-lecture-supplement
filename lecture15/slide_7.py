def is_weekend(day):
    return day > 5

def is_awake(hour, day):
    if is_weekend(day):
        if hour > 12 or hour < 2:
            return True
    elif hour > 8 and hour < 24:
        return True

    return False

if __name__ == '__main__':
    print(is_awake(14, 6))
    print(is_awake(14, 3))
    print(is_awake(24, 3))
    print(is_awake(24, 6))