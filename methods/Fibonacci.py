import math

from methods.NumericalMethod import numericalMethod


class fibonacci(numericalMethod):
    n = 11

    def __init__(self, targetFunction, a, b, delta, eps, n):
        super().__init__(targetFunction, a, b, delta, eps)
        self.n = n

    def fibonacciNumbers(self, n):
        F1 = 1
        F2 = 1
        for __ in range(n):
            F1, F2 = F2, F1 + F2

        return F1


    # Override
    def numericalSolution(self):
        iteration = 0
        left = self.a
        right = self.b

        Fn = self.fibonacciNumbers(self.n)
        l1 = right - left
        l2 = self.fibonacciNumbers(self.n - 1) / Fn * l1 + math.pow(-1, self.n) * self.eps / Fn
        x2 = left + l2

        k = 1
        while k < self.n:
            x1 = left + right - x2
            Q1 = self.Q(x1)
            Q2 = self.Q(x2)

            if (x1 < x2 and Q1 < Q2):
                right = x2
                x2 = x1
                Q2 = Q1
            elif (x1 > x2 and Q1 < Q2):
                left = x2
                x2 = x1
                Q2 = Q1
            elif (x1 < x2 and Q1 >= Q2):
                left = x1
            elif (x1 > x2 and Q1 >= Q2):
                right = x1

            k += 1
            iteration += 1
            self.solution[iteration] = [iteration, left, right, self.Q(left), self.Q(right)]

        # Last iteration
        x2 += self.eps
        Q1 = self.Q(x1)
        Q2 = self.Q(x2)

        if (x1 < x2 and Q1 < Q2):
            right = x2
        elif (x1 > x2 and Q1 < Q2):
            left = x2
        elif (x1 < x2 and Q1 >= Q2):
            left = x1
        elif (x1 > x2 and Q1 >= Q2):
            right = x1

        iteration += 1
        self.solution[iteration] = [iteration, left, right, self.Q(left), self.Q(right)]

        # Reference data
        self.N = iteration
        self.solutionEval = [left, right]
        self.x_ = (left + right) / 2
        self.Q_ = self.Q(self.x_)
