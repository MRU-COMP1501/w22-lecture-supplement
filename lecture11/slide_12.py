def get_lowest_3(grades):
    grades.sort()
    return grades[0:3]

def get_lowest(grades, n):
    grades.sort()
    return grades[0:n]

def get_highest(grades, n):
    grades.sort()
    grades.reverse()
    return grades[0:n]

def get_highest_alt(grades, n):
    grades.sort()
    return grades[len(grades) - 3:]

def main():
    grades = [9, 9, 8, 9, 7, 6.5, 2, 6]
    print(get_lowest_3(grades))
    print(get_lowest(grades, 5))
    print(get_highest(grades, 3))
    print(get_highest_alt(grades, 3))

main()