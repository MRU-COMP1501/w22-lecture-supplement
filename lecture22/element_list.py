from element import Element

def read_element_list(filename):
    try:
        f_obj = open(filename, 'r')
    except OSError:
        print("Something went wrong opening " + filename)
        return []
    
    header = f_obj.readline() # not used, but we need to read past it
    elements = []
    for line in f_obj:
        vals = line.split(',')
        try:
            number = int(vals[0])
            name = vals[1] # Name currently not used in Element class
            symbol = vals[2]
            mass = float(vals[3])
            electrons = int(vals[4])
            elements.append([symbol, number, mass, electrons])
        except ValueError as e:
            print(e)
            print(line)

    f_obj.close()
    return elements

def read_elements(filename):
    try:
        f_obj = open(filename, 'r')
    except OSError:
        print("Something went wrong opening " + filename)
        return []
    
    header = f_obj.readline() # not used, but we need to read past it
    elements = []
    for line in f_obj:
        vals = line.split(',')
        try:
            number = int(vals[0])
            name = vals[1] # Name currently not used in Element class
            symbol = vals[2]
            mass = float(vals[3])
            electrons = int(vals[4])
            element = Element(symbol, number, mass, electrons)
            elements.append(element)
        except ValueError as e:
            print(e)
            print(line)

    f_obj.close()
    return elements

def find_element(elements, number):
    for element in elements:
        if element.get_number() == number:
            return element.get_symbol()
    

if __name__ == '__main__':
    element_list = read_element_list('lecture22/periodic_table.csv')
    element_list.sort()
    for element in element_list[:5]:
        print(element)

    elements = read_elements('lecture22/periodic_table.csv')
    # elements.sort() # Runtime error
    for element in elements[:5]:
        print(element)
    
    number = int(input('What atomic number do you want to find? '))
    print(find_element(elements, number))
