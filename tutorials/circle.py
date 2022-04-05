from math import pi

class Circle:
    def __init__(self, radius, centre=(0, 0)):
        self.__radius = radius
        # self.set_radius(radius) # alternative way of setting __radius
        self.__centre = centre
    
    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        self.__radius = radius
    
    def get_centre(self):
        return self.__centre
    
    def set_centre(self, centre):
        self.__centre = centre

    def area(self):
        return pi * self.__radius ** 2
    
    def __str__(self):
        return (f'Circle with radius {self.__radius}'
                f' and centre {self.__centre}')

if __name__ == '__main__':
    circle = Circle(10)
    print(circle)
    print(circle.area())
    circle.set_radius(5)
    print(circle)
    print(circle.area())