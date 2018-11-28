import matplotlib.pylab as plt
import numpy as np
from py_expression_eval import Parser
from tabulate import tabulate
from abc import ABC, ABCMeta, abstractmethod


class numericalMethod(ABC):
    __metaclass__ = ABCMeta

    targetExpression = 'x^2 + 47'
    a = -1
    b = 1
    delta = 0.01
    eps = 0.001

    solution = {}
    N = 0
    solutionEval = []
    x_ = 0
    Q_ = 0

    def __init__(self, targetFunction, a, b, delta, eps):
        self.targetExpression = targetFunction
        self.a = a
        self.b = b
        self.delta = delta
        self.eps = eps

        self.expression = Parser().parse(self.targetExpression)


    def Q(self, x):
        return self.expression.evaluate({'x': x})


    def printExpression(self):
        print('Q(x) = ' + self.targetExpression)


    def initPlot(self, namePlot, step):
        x = np.arange(self.a, self.b + step, step)
        y = []
        for args in x:
            y.append(self.Q(args))

        plt.figure(namePlot)
        plt.xlabel('x')
        plt.ylabel('Q(x)')
        plt.plot(x, y, label=self.targetExpression)
        plt.legend()

        return plt


    def showFunction(self):
        self.initPlot('Target function', 0.01).show()


    def showNumericalMethod(self):
        newPlot = self.initPlot('Work of the numerical method', 0.01)
        for values in self.solution.values():
            newPlot.plot(values[1], values[3], 'go')
            newPlot.plot(values[2], values[4], 'go')

        newPlot.plot(self.x_, self.Q_, 'rs', label='optimum')
        newPlot.show()


    def showTable(self):
        print(tabulate(list(self.solution.values()), headers=['№ iter', 'a', 'b', 'Q(a)', 'Q(b)'], tablefmt='orgtbl'))


    def showReference(self):
        print('->Input:')
        print('--->Q(x) = ' + self.targetExpression)
        print('--->[a, b] = [', self.a, ',', self.b, ']')
        print('--->delta = ', self.delta)
        print('--->eps = ', self.eps)

        print('->Output:')
        print('--->Iterations: ', self.N)
        print('--->Evaluation of the solution: ', self.solutionEval)
        print('--->x* = ', self.x_)
        print('--->Q(x*) = ', self.Q_)


    @abstractmethod
    def numericalSolution(self):
        pass
