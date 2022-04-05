from circle import Circle
from rectangle import Rectangle

def get_larger(circ_1, circ_2):
    if circ_1.get_radius() > circ_2.get_radius():
        return circ_1
    else:
        return circ_2

def overlap(circ_1, circ_2):
    """
    Returns True if the two circles overlap, False otherwise.
    """
    # get the two centres and radii, then check for overlap by comparing
    # the distance between the centres and the sum of the radii
    distance = ((circ_1.get_centre()[0] - circ_2.get_centre()[0]) ** 2 +
                (circ_1.get_centre()[1] - circ_2.get_centre()[1]) ** 2) ** 0.5
    return distance <= circ_1.get_radius() + circ_2.get_radius()

def rect_largest(rect_1, rect_2):
    """
    Returns the largest rectangle.
    """
    if rect_1.area() > rect_2.area():
        return rect_1
    else:
        return rect_2

def rect_overlap(rect_1, rect_2):
    """
    Returns True if the two rectangles overlap, False otherwise.
    """
    # get the two centres and width/height. Then check for overlap by
    # comparing the distance between the centres and the sum of the
    # widths/heights
    centre_1 = rect_1.get_centre()
    centre_2 = rect_2.get_centre()
    x_dist = abs(centre_1[0] - centre_2[0])
    y_dist = abs(centre_1[1] - centre_2[1])
    return ((x_dist <= (rect_1.get_width() + rect_2.get_width()) / 2 and
             y_dist <= (rect_1.get_height() + rect_2.get_height()) / 2))


def main():
    circle_1 = Circle(10.5, (0, 0))
    circle_2 = Circle(3, (8, 2))
    print(circle_1)
    print(circle_2)
    print(f'The largest is {get_larger(circle_1, circle_2)}')
    print(f'Overlap: {overlap(circle_1, circle_2)}')
    rect_1 = Rectangle(10, 5, (0, 0))
    rect_2 = Rectangle(2, 8, (6, 2))
    print(rect_1)
    print(rect_2)
    print(f'The largest is {rect_largest(rect_1, rect_2)}')
    print(f'Overlap: {rect_overlap(rect_1, rect_2)}')

if __name__ == '__main__':
    main()