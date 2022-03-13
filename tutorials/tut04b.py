from math import acos, sin, cos, radians

EARTH_RAD = 6371.01
# read lat and long for two points from the user
# calculate distance between the points
# display the distance

def calculate_distance(t1, g1, t2, g2):
    t1 = radians(t1)
    g1 = radians(g1)
    t2 = radians(t2)
    g2 = radians(g2)

    # https://www.w3schools.com/python/ref_math_acos.asp
    distance = EARTH_RAD * acos(
        sin(t1) * sin(t2) 
        + cos(t1) * cos(t2) * cos(g1 - g2)
    )
    return distance

def main():
    t1 = float(input('Enter the latitude for point 1: '))
    g1 = float(input('Enter the longitude for point 1: '))
    t2 = float(input('Enter the latitude for point 2: '))
    g2 = float(input('Enter the longitude for point 2: '))

    distance = calculate_distance(t1, g1, t2, g2)
    print(f'The distance is {distance:.2f}')

main()