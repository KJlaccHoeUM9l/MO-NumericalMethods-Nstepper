from methods.NumericalMethod import numericalMethod


class dichotomy1(numericalMethod):
    # Override
    def numericalSolution(self):
        iteration = 0
        left = self.a
        right = self.b

        while right - left > self.delta:
            x1 = (left + right) / 2 - self.eps
            x2 = (left + right) / 2 + self.eps

            Q1 = self.Q(x1)
            Q2 = self.Q(x2)

            if Q1 < Q2:
                right = x2
            else:
                left = x1

            iteration += 1
            self.solution.append([iteration, left, right, self.Q(left), self.Q(right)])

        # Reference data
        self.N = iteration
        self.solutionEval = [left, right]
        self.x_ = (left + right) / 2
        self.Q_ = self.Q(self.x_)
