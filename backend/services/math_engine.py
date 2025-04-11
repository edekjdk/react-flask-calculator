import sympy as sy


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

    def integrate(self, expression) -> str:
        self.sympy_expression = sy.sympify(expression)
        self.integral = sy.integrate(self.sympy_expression)
        self.latex_output = sy.latex(self.integral)
        self.result = {"output": self.integral, "latex_output": self.latex_output}
        return self.result

    def differentiate(self, expression: str) -> str:
        self.sympy_expression = sy.sympify(expression)
        self.derivative = sy.diff(self.sympy_expression)
        self.latex_output = sy.latex(self.derivative)
        self.result = {"output": self.derivative, "latex_output": self.latex_output}
        return self.result

        return "differentiate {}".format(expression)

    def plot(self, expression: str) -> str:
        return "plot {}".format(expression)

    def calculate(self, expression: str) -> str:
        return "calculate {}".format(expression)
