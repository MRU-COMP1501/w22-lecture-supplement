def is_enough_cookies(cookies, people):
    if people > 0 and cookies / people > 1:
        return True
    else:
        return False

if __name__ == '__main__':
    cookies = 4
    people = 2
    print(is_enough_cookies(cookies, people))
    people = 0
    print(is_enough_cookies(cookies, people))
