from polynomialTEST import *

def close_to_zero(value: float, epsilon: float) -> bool:
    return value <= epsilon and value >= -1 * epsilon

# f(p) MUST be negative and f(q) MUST be positive, otherwise it's UB
def get_zero(function: PolynomialFunction, p: float, q: float, epsilon: float) -> float:
    pivot = (p + q) / 2
    value = function.get_value(pivot)

    if(close_to_zero(value, epsilon)):
        return pivot
    if(value > 0):
        return get_zero(function, p, pivot, epsilon)
    return  get_zero(function, pivot, q, epsilon)

def get_zeros(function: PolynomialFunction, p: float, q: float, epsilon: float, sections: int) -> list:
    delta = (q - p) / sections
    zeros = []
    ptr_old = p
    value_old = function.get_value(ptr_old)

    for i in range(0, sections):
        ptr_new = ptr_old + delta
        value_new = function.get_value(ptr_new)
        if(value_old < 0 and value_new > 0):
            zeros.append(get_zero(function, ptr_old, ptr_new, epsilon))
        elif(value_old > 0 and value_new < 0):
            zeros.append(get_zero(function, ptr_new, ptr_old, epsilon))

        ptr_old = ptr_new
        value_old = value_new

    return zeros
