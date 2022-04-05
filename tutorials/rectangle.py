class Rectangle:
    def __init__(self, width, height, centre=(0, 0)):
        self.__width = width
        self.__height = height
        self.__centre = centre
    
    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height
    
    def get_centre(self):
        return self.__centre
    
    def set_width(self, width):
        self.__width = width
    
    def set_height(self, height):
        self.__height = height
    
    def set_centre(self, centre):
        self.__centre = centre
    
    def area(self):
        return self.__width * self.__height
    
    def __str__(self):
        return (f'Rectangle with width {self.__width} and height {self.__height}'
                f' and centre {self.__centre}')
    
if __name__ == '__main__':
    rect = Rectangle(10, 5)
    print(rect)
    print(rect.area())
    rect.set_width(2)
    rect.set_height(8)
    rect.set_centre((1, 1))
    print(rect)
    print(rect.area())