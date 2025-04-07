from backend.services import Expression_processor


class Test_Experssion_processor:
    def test(self):
        # try
        test = Expression_processor("w(sin(x))")
        test2 = Expression_processor("c(123)")

        # when
        assert test.mode == "plot"
        assert test.get_inner_expression() == "sin(x)"
        assert test2.mode == "integrate"
        assert test2.get_inner_expression() == "123"

    def test2(self):
        # try
        test = Expression_processor("c(xd)")
        assert test.mode == "integrate"

    def test_calculate(self):
        test = Expression_processor("12+3")

        assert test.mode == "calculate"
        assert test.get_inner_expression() == "12+3"
