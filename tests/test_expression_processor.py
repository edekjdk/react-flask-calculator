from backend.services import Expression_processor


class TestExpressionProcessor:
    def test_plot(self):
        # Test for 'plot' mode
        test = Expression_processor("plot(sin(x))")
        assert test.mode == "plot"
        assert test.get_inner_expression() == "sin(x)"

    def test_integrate(self):
        # Test for 'integrate' mode
        test = Expression_processor("integrate(x^2)")
        assert test.mode == "integrate"
        assert test.get_inner_expression() == "x^2"

    def test_integrate_int(self):
        # Test for 'integrate' with int()
        test = Expression_processor("int(123)")
        assert test.mode == "integrate"
        assert test.get_inner_expression() == "123"

    def test_differentiate(self):
        # Test for 'differentiate' mode
        test = Expression_processor("diff(x^2)")
        assert test.mode == "differentiate"
        assert test.get_inner_expression() == "x^2"

    def test_calculate(self):
        # Test for 'calculate' mode
        test = Expression_processor("12 + 3")
        assert test.mode == "calculate"
        assert test.get_inner_expression() == "12+3"

    def test_diff_int(self):
        # Test for 'differentiate' with int() inside
        test = Expression_processor("diff(int(5))")
        assert test.mode == "differentiate"
        assert test.get_inner_expression() == "int(5)"

    def test_empty_input(self):
        # Test for empty input
        test = Expression_processor("")
        assert test.mode == "calculate"
        assert test.get_inner_expression() == ""

    def test_invalid_expression(self):
        # Test for an invalid expression (unexpected input)
        test = Expression_processor("invalid_expression()")
        assert test.mode == "calculate"
        assert test.get_inner_expression() == "invalid_expression()"

    def test_parentheses(self):
        # Test for parentheses handling
        test = Expression_processor("plot((sin(x)))")
        assert test.mode == "plot"
        assert test.get_inner_expression() == "(sin(x))"

    def test_unknown_function(self):
        # Test for an unknown function (should be treated as 'calculate')
        test = Expression_processor("unknown_function(5)")
        assert test.mode == "calculate"
        assert test.get_inner_expression() == "unknown_function(5)"
