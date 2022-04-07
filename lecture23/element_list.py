from element import Element

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

def swap_adjacent(elements):
    changing = False
    for i in range(1, len(elements)):
        prev = elements[i - 1]
        if prev.get_electrons() < elements[i].get_electrons():
            elements[i - 1] = elements[i]
            elements[i] = prev
            changing = True
    return changing

def sort(elements):
    go_go_go = True
    while go_go_go:
        print('Next iteration: ')
        for element in elements[:5]:
            print(element)
        print('   ')
        go_go_go = swap_adjacent(elements)

if __name__ == '__main__':
    elements = read_elements('lecture22/periodic_table.csv')
    # elements.sort() # Runtime error
    for element in elements[:5]:
        print(element)
    
    sort(elements)
