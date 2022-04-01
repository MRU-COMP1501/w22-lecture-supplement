from math import pi

class Circle:
    def __init__(self, radius):
        # self.__radius = radius # same as next line
        self.set_radius(radius)
    
    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        self.__radius = radius

    def area(self):
        return pi * self.__radius ** 2
    
    def __str__(self):
        return f'Circle with radius {self.__radius}'

if __name__ == '__main__':
    circle = Circle(10)
    print(circle)
    print(circle.area())
    circle.set_radius(5)
    print(circle)
    print(circle.area())