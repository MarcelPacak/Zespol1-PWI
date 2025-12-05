from .Vector import Vector

class Polynomial:
    def get_value(x, y):
        return x**2 + 2*y**2 - 1

def get_points(polynomial: Polynomial, left_down_corner: Vector, right_up_corner: Vector, height_accuracy: int, width_accuracy: int) -> list:
    kwadraciki = [[0 for i in range(d)] for i in range(d)]
    
