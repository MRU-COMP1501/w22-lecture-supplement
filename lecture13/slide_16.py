def is_water_boiling(city, temp):
    if city == 'Calgary' and temp > 96.2:
        return True
    
    if city == 'Vancouver' and temp > 100:
        return True

    # If we reach this point, the other two conditions are false
    # Maybe we don't know the city, so just check temperature 
    if temp > 100:
        return True
    else:
        return False

def is_water_liquid(city, temp):
    boiling_point = 100
    if city == 'Calgary':
        boiling_point = 96.2
    # else:
    #     boiling_point = 100

    if temp > 0 and temp < boiling_point:
        return True
    else:
        return False

if __name__ == '__main__':
    city = input("Enter the city: ")
    temp = float(input("Enter the water temp: "))
    print('Boiling:', is_water_boiling(city, temp))
    print('Liquid:', is_water_liquid(city, temp))