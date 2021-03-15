import pytest


@pytest.mark.usefixtures("data_calculator")
@pytest.mark.usefixtures("data_parameterized")
class TestCalculator:
    # def test_addition(self, data_calculator):
    #     print(f"Addition of {data_calculator[0]},{data_calculator[1]}: {data_calculator[0] + data_calculator[1]}")
    #
    # def test_subtraction(self, data_calculator):
    #     print(f"Subtraction of {data_calculator[0]},{data_calculator[1]}: {data_calculator[0] - data_calculator[1]}")
    #
    # def test_multiplication(self, data_calculator): print(f"Multiplication of {data_calculator[0]},
    # {data_calculator[1]}: {data_calculator[0] * data_calculator[1]}")
    #
    def test_addition(self, data_parameterized):
        print(
            f"Addition of {data_parameterized[0]},{data_parameterized[1]}: {data_parameterized[0] + data_parameterized[1]}")

    def test_subtraction(self, data_parameterized):
        print(
            f"Subtraction of {data_parameterized[0]},{data_parameterized[1]}: {data_parameterized[0] - data_parameterized[1]}")

    def test_multiplication(self, data_parameterized):
        print(
            f"Multiplication of {data_parameterized[0]},{data_parameterized[1]}: {data_parameterized[0] * data_parameterized[1]}")
