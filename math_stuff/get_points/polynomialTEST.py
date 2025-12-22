class Polynomial:
    def get_value(x, y):
        return x * y**3 + x**2 * y + 1

    def set_x(self, x):
        return PolynomialFunctionSetX(self, x)

    def set_y(self, y):
        return PolynomialFunctionSetY(self, y)


class PolynomialFunction:
    def get_value(x):
        pass

class PolynomialFunctionSetX:
    def __init__(self, polynomial, x):
        self.Polynomial = Polynomial
        self.x = x

    def get_value(self, x):
        return Polynomial.get_value(self.x, x)

class PolynomialFunctionSetY:
    def __init__(self, polynomial, y):
        self.Polynomial = Polynomial
        self.y = y

    def get_value(self, x):
        return Polynomial.get_value(x, self.y)