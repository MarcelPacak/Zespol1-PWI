class Polynomial1:
    def __init__(self, degree: int):
        self.coeff_list = [0] * (degree + 1)
        self.degree = degree

    def add(self, coeff:float, x_exp: int):
        self.coeff_list[x_exp] += coeff

    def get_value(self, x: float) -> float:
        value = 0
        for i in range(self.degree, -1, -1):
            value *= x
            value += self.coeff_list[i]

        return value

class Polynomial2:
    def __init__(self):
        self.dictionary = {} # key jest dwuelementowym tuplem oznaczajacym potege, kolejno, przy x oraz y, a wartosc to wspolczynnik ktory tam stoi
        self.max_x_exp = 0
        self.max_y_exp = 0

    def add(self, coeff: float, x_exp: int, y_exp: int):
        key = (x_exp, y_exp)
        self.dictionary.setdefault(key, 0)
        self.dictionary[key] += coeff

        self.max_x_exp = max(self.max_x_exp, x_exp)
        self.max_y_exp = max(self.max_y_exp, y_exp)

    #zwracanie wielomianu jednej zmiennej x lub ys:

    def set_x(self, x: float) -> Polynomial1:
        new_poly = Polynomial1(self.max_y_exp)
        for key, value in self.dictionary.items():
            new_poly.add(value * x**key[0], key[1])
        return new_poly

    def set_y(self, y: float) -> Polynomial1:
        new_poly = Polynomial1(self.max_x_exp)
        for key, value in self.dictionary.items():
            new_poly.add(value * y**key[1], key[0])
        return new_poly
