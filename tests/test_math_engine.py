from backend.services import MathEngine


class TestMathEngine:
    def test(self):
        test = MathEngine("sin(x)", "integrate")
        assert test.evaluate()["output"] == "-cos(x)"

    def test_simple_differentiate(self):
        test = MathEngine("x**2", "differentiate")
        assert test.evaluate()["output"] == "2*x"

    def test_simple_differentiate2(self):
        test = MathEngine("x^2", "differentiate")
        assert test.evaluate()["output"] == "2*x"

    def test_integrate_constant(self):
        test = MathEngine("5", "integrate")
        assert test.evaluate()["output"] == "5*x"

    def test_differentiate_constant(self):
        test = MathEngine("42", "differentiate")
        assert test.evaluate()["output"] == "0"

    def test_differentiate_zero(self):
        test = MathEngine("0", "differentiate")
        assert test.evaluate()["output"] == "0"

    def test_weird_spacing(self):
        test = MathEngine("   x ^  3   ", "differentiate")
        assert test.evaluate()["output"] == "3*x**2"
