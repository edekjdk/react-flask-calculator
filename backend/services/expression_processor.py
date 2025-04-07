class Expression_processor:
    def __init__(self, expression: str):
        self.expression = expression.strip()
        self.mode = self.detect_mode()

    def detect_mode(self) -> str:
        if self.expression.startswith("c("):
            return "integrate"
        elif self.expression.startswith("p("):
            return "differentiate"
        elif self.expression.startswith("w("):
            return "plot"
        else:
            return "calculate"

    def get_inner_expression(self) -> str:
        if self.mode != "calculate":
            return self.expression[2:-1]
        else:
            return self.expression
