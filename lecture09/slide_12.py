import math

def modify_me(a, b):
    c = average(2, 3)
    return c

def average(a, b):
    return (a + b) / 2

def abs_diff(a, b):
    return math.abs(a - b)

def main():
    a = average(3, 4)
    b = abs_diff(3, 4)

main()