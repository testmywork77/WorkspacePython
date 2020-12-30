import pytest

# Test case with Passed Test
@pytest.mark.math
def test_one_plus_one():
    assert 1 + 1 == 2

# Test case with Failed Test,  A test function to show assertion introspection
@pytest.mark.math
def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c

# Test case with Runtime Exception, A test function that verfies an exception
@pytest.mark.math
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1/0
    
    assert 'division by zero' in str(e.value)

# Parameterized Test Case, A parametrized test function
products = [
  (2, 3, 6),            # postive integers
  (1, 99, 99),          # identity
  (0, 99, 0),           # zero
  (3, -4, -12),         # positive by negative
  (-5, -5, 25),         # negative by negative
  (2.5, 6.7, 16.75)     # floats
]

@pytest.mark.math
@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product