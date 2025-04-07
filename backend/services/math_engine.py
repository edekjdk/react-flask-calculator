class MathEngine:
    def __init__(self, inner_expression: str, mode: str):
        self.inner_expression = inner_expression
        self.mode = mode

    def evaluate(self):
        if self.mode == "integrate":
            return self.integrate(self.inner_expression)
        elif self.mode == "differentiate":
            return self.differentiate(self.inner_expression)
        elif self.mode == "plot":
            return self.plot(self.inner_expression)
        else:
            return self.calculate(self.inner_expression)

    def integrate(self, expression: str) -> str:
        return "integrate {}".format(expression)

    def differentiate(self, expression: str) -> str:
        return "differentiate {}".format(expression)

    def plot(self, expression: str) -> str:
        return "plot {}".format(expression)

    def calculate(self, expression: str) -> str:
        return "calculate {}".format(expression)
