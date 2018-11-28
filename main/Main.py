from methods.Dichotomy1 import dichotomy1
from methods.Fibonacci import fibonacci

EXIT = 0
BACK = 9
INPUT = 1
METHODS = 2
DICHOTOMY = 2
FIBONACCI = 3


def useMethod(method):
    method.numericalSolution()
    print('')
    print('---------- REFERENCE ----------')
    method.showReference()
    method.showTable()
    method.showNumericalMethod()

if __name__ == '__main__':
    global method
    targetFunction = 'x^2 + 47'
    a = -1
    b = 1
    delta = 0.001
    eps = 0.00001
    n = 11

    select = -1
    while (select != EXIT):
        print('SELECT ACTION:')
        print(INPUT, ' - INPUT task conditions')
        print(METHODS, ' - select METHOD')
        print(EXIT, ' - EXIT')
        select = int(input('Your action: '))

        if select == INPUT:
            targetFunction = input('Enter target function Q(x) = ')
            a = float(input('Enter left boundary[a]: '))
            b = float(input('Enter right boundary[b]: '))
        elif select == METHODS:
            met = 47
            while met != BACK:
                print('SELECT METHOD:')
                print(DICHOTOMY, ' - use DICHOTOMY-1 method')
                print(FIBONACCI, ' - use FIBONACCI method')
                print(BACK, ' - BACK')
                met = int(input('Your choose: '))

                if met == DICHOTOMY:
                    print('********************* DICHOTOMY 1 *********************')
                    delta = float(input('Enter precision of method[delta]: '))
                    eps = float(input('Enter parameter of method[eps]: '))
                    if (eps > delta / 100):
                        print('eps = ', eps, ' -> ', delta / 100)
                        eps = delta / 100
                    useMethod(dichotomy1(targetFunction, a, b, delta, eps))
                    print('*******************************************************')
                elif met == FIBONACCI:
                    print('********************** FIBONACCI **********************')
                    n = int(input('Enter quantity of steps[n]: '))
                    eps = float(input('Enter parameter of method[eps]: '))
                    useMethod(fibonacci(targetFunction, a, b, delta, eps, n))
                    print('*******************************************************')
