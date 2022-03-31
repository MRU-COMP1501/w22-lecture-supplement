class Element:
    def __init__(self, symbol, number, mass):
        self.__symbol = symbol
        self.__number = number
        self.__mass = mass

    def set_symbol(self, new_symbol):
        print('Sorry, cannot change a symbol')
        # self.__symbol = new_symbol # actually setting the symbol

    def get_symbol(self):
        return self.__symbol

    def get_number(self):
        return self.__number

if __name__ == '__main__':
    hydrogen = Element('H', 1, 1.01)
    # helium = Element()
    hydrogen2 = hydrogen # create a new reference to the hydrogen object
    print(hydrogen)
    # hydrogen.flavour = 'strawberry'
    hydrogen.set_symbol('Bob')
    print('The symbol for hydrogen is', hydrogen.get_symbol())
    print('The number for hydrogen is', hydrogen.get_number())
    hydrogen.__number = 100
    print('The number for hydrogen is', hydrogen.get_number())
    # print(hydrogen.flavour)
    # print(helium)