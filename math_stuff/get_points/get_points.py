# TEST
class Polynomial:
    def get_value(x, y):
        return x * y**3 + x**2 * y + 1

    def set_x(x):
        return


class PolymonialFunction:
    degree = 3
    def get_value(x):
        return -3 * x**3 + 9 * x + 0.5
# TEST

from ..math_objects import *

def get_points(polynomial: Polynomial, left_down_corner: Vector, right_up_corner: Vector, epsilon: float) -> list:
    signs = []
