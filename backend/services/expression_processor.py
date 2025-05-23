class Expression_processor:
    def __init__(self, expression: str):
        self.expression = self.prepare_expression(expression)
        self.mode = self.detect_mode()

    def detect_mode(self) -> str:
        if self.expression.startswith("integrate(") or self.expression.startswith(
            "int("
        ):
            return "integrate"
        elif self.expression.startswith("differentiate(") or self.expression.startswith(
            "diff("
        ):
            return "differentiate"
        elif self.expression.startswith("plot("):
            return "plot"
        else:
            return "calculate"

    def get_inner_expression(self) -> str:
        if self.mode != "calculate":
            return self.expression[self.expression.index("(") + 1 : -1]
        else:
            return self.expression

    def prepare_expression(self, expression):
        self.prepared_expression = (
            expression.strip().replace(" ", "").replace("^", "**")
        )
        return self.prepared_expression
