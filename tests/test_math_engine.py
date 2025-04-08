from backend.services import MathEngine


class TestMathEngine:
    def test(self):
        test = MathEngine("sin(x)", "integrate")
        assert test.evaluate() == "integrate sin(x)"
