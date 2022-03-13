import math
EARTH_RAD = 6371.01

# read lat and long from user for two points
# calculate distance between points
# display result

def calc_distance(t1, g1, t2, g2):
    # from https://www.geeksforgeeks.org/python-math-acos-function/#:~:text=acos()%20function%20returns%20the,in%20between%20%2D1%20to%201.&text=Parameter%3AThis%20method%20accepts%20only%20single%20parameters.&text=Returns%3AThis%20function%20returns%20the%20arc%20cosine%20value%20of%20a%20number.
    t1 = math.radians(t1)
    g1 = math.radians(g1)
    t2 = math.radians(t2)
    g2 = math.radians(g2)
    distance = EARTH_RAD * math.acos(
        math.sin(t1) * math.sin(t2)
        + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2)
    )
    return distance

def main():
    t1 = float(input('Enter the latitude for point 1: '))
    g1 = float(input('Enter the longitude for point 1: '))
    t2 = float(input('Enter the latitude for point 2: '))
    g2 = float(input('Enter the longitude for point 2: '))

    distance = calc_distance(t1, g1, t2, g2)

    print(f'The distance is {distance:.2f}')

main()