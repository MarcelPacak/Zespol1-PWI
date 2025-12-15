class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Matrix:
    def __init__(self, a: float, b: float, c: float, d: float):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def times(self, vector: Vector) -> Vector:
        new_vector = Vector(0, 0)
        new_vector.x = self.a * vector.x + self.b * vector.y
        new_vector.y = self.c * vector.x + self.d * vector.y
        return new_vector