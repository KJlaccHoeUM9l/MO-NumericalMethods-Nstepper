from methods.Dichotomy1 import dichotomy1
from methods.Fibonacci import fibonacci

if __name__ == '__main__':

    targetFunction = 'x^2 - 1'
    a = -2
    b = 2
    delta = 0.001
    eps = 0.00001

    n = 17

    #method = dichotomy1(targetFunction, a, b, delta, eps)
    method = fibonacci(targetFunction, a, b, delta, eps, n)

    method.numericalSolution()
    method.showReference()
    method.showTable()
    method.showNumericalMethod()
