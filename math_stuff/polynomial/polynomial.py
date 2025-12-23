class Elements:
    def __init__(self, coeff, x_exp, y_exp): # przykladowo dla 3*x^2*y^1 (3, 2, 1)
        self.coeff = coeff
        self.x_exp = x_exp
        self.y_exp = y_exp

class Polynomial:
    def __init__(self, list_of_elements):
        self.list_of_elements = list_of_elements
    
    def calc_polynomial(self, x: float, y: float):
        result = 0
        for i in self.list_of_elements:
            result += coeff * (x ** x_exp) * (y ** y_exp)
        return result


    def set_x(self): #zwracanie wielomianu jednej zmiennej x lub y
        pass
    #zwracany obiekt ma miec nazwe PolynomialFunction

    def set_y(self): 
        pass