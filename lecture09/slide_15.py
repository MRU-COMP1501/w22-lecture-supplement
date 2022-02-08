def f(x):
    x = x * 3
    return g(x)

def g(y):
    return y * 2

def main():
    x = 5
    y = 10
    print('Before') # What are the values of x, y, and z before calling f?
    z = f(x)
    print('After') # What are the values of x, y, and z after calling f?

main()
