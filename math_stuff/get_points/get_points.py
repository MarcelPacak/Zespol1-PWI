from math_stuff.polynomial.polynomial import *
from .get_zeros import get_zeros

def float_range(start: float, stop: float, step: float):
    while(start < stop):
        yield start
        start += step

def get_points(polynomial: Polynomial2, left_down_corner: tuple, right_up_corner: tuple, epsilon: float, horizontal_sections: int, vertical_sections: int) -> list:
    points = []
    
    # X axis
    width = abs(left_down_corner[0] - right_up_corner[0])
    delta = width / vertical_sections

    for i in float_range(left_down_corner[0] + delta / 2, right_up_corner[0], delta):
        polyFunc = polynomial.set_x(i)
        for j in get_zeros(polyFunc, left_down_corner[1], right_up_corner[1], epsilon, horizontal_sections):
            points.append( (i, j) )

    # Y axis
    height = abs(left_down_corner[1] - right_up_corner[1])
    delta = height / horizontal_sections

    for i in float_range(left_down_corner[1] + delta / 2, right_up_corner[1], delta):
        polyFunc = polynomial.set_y(i)
        for j in get_zeros(polyFunc, left_down_corner[0], right_up_corner[0], epsilon, vertical_sections):
            points.append( (j, i) )

    return points
