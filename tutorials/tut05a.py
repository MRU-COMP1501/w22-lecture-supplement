from math import acos, sin, cos, radians

EARTH_RAD = 6371.01
# read lat and long for two points from the user
# calculate distance between the points
# display the distance

def calculate_distance(pt1, pt2): #t1, g1, t2, g2):
    t1 = radians(pt1[0])
    g1 = radians(pt1[1])
    t2 = radians(pt2[0])
    g2 = radians(pt2[1])

    # https://www.w3schools.com/python/ref_math_acos.asp
    distance = EARTH_RAD * acos(
        sin(t1) * sin(t2) 
        + cos(t1) * cos(t2) * cos(g1 - g2)
    )
    return distance

def read_coordinates(coord_num):
    coord_str = input(f'Enter the coordinates for point {coord_num}: ')
    list_str = coord_str.split(',')
    coords = []
    for num_str in list_str:
        num = float(num_str)
        coords.append(num)
    return coords

def main():
    pt1 = read_coordinates(1)
    pt2 = read_coordinates(2)

    distance = calculate_distance(pt1, pt2)
    print(f'The distance is {distance:.2f}')

main()