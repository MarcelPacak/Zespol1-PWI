class OneElement:
    def __init__(self, coeff, x_exp):
        self.coeff = coeff
        self.x_exp = x_exp

class PolynomialFunction:
    def __init__(self, list_of_elements, x : float):
        self.list_of_elements = list_of_elements
        self.x = x


class Elements:
    def __init__(self, coeff, x_exp, y_exp): # przykladowo dla 3*x^2*y^1 (3, 2, 1)
        self.coeff = coeff
        self.x_exp = x_exp
        self.y_exp = y_exp

class Polynomial:
    def __init__(self, list_of_elements):
        self.list_of_elements = list_of_elements
    
    def get_value(self, x: float, y: float):
        result = 0
        for coeff, x_exp, y_exp in self.list_of_elements:
            result += coeff * (x ** x_exp) * (y ** y_exp)
        return result


    def set_x(self, x: float): #zwracanie wielomianu jednej zmiennej x lub y
        list_of_set_x = []
        for coeff, x_exp, y_exp in self.list_of_elements:
            new_element = OneElement(coeff * (x ** x_exp), y_exp)
            list_of_set_x.append(new_element)
        PolynomialFunctionX = PolynomialFunction(list_of_set_x, x)
        return PolynomialFunctionX

    def set_y(self, y: float): 
        list_of_set_y = []
        for coeff, x_exp, y_exp in self.list_of_elements:
            new_element = OneElement(coeff * (y ** y_exp), x_exp)
            list_of_set_y.append(new_element)
        PolynomialFunctionY = PolynomialFunction(list_of_set_y, y)
        return PolynomialFunctionY