import pytest

# --------------------------------------------------------------------------------
# A test function that verifies an exception (ZeroDivisionError: division by zero)
# --------------------------------------------------------------------------------

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0 

    assert 'division by zero' in str(e.value)