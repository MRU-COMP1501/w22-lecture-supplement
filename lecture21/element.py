class Element:
    """
    Represents a chemical element.

    Fields:
        symbol: a string representing the chemical symbol of the element
        number: an integer representing the atomic number of the element
        mass: a float representing the atomic mass of the element
        electrons: an integer representing the number of electrons in the element
    """
    def __init__(self, symbol, number, mass, electrons):
        """
        Constructor for an element.
        """
        self.__symbol = symbol
        self.__number = number
        self.__mass = mass
        self.__electrons = electrons

    def get_symbol(self):
        return self.__symbol
    
    def get_number(self):
        return self.__number
    
    def get_mass(self):
        return self.__mass
    
    def get_electrons(self):
        return self.__electrons
    
    def get_neutrons(self):
        return int(self.__mass - self.__number)

    def __str__(self):
        # return 'I am an Element'
        return (f'{self.__symbol}: ' 
                f'Number {self.__number}, ' 
                f'Mass: {self.__mass}')

if __name__ == '__main__':
    hydrogen = Element('H', 1, 1.01, 1)
    helium = Element('He', 2, 4.002, 2)

    print(helium.get_neutrons())
    print(helium)
    print(hydrogen)
    print('Hydrogen is ' + str(hydrogen))