import pytest


# pytest file should start with test_* or ends with *_test
# pytest method names should start with test_
# code should be wrapped in method only
@pytest.mark.smoke
def test_firstDemo2():
    print("demo2_test.py -> test_firstDemo2")


@pytest.mark.sanity
def test_secondDemo2():
    print("demo2_test.py -> def test_secondDemo2")


@pytest.mark.regression
def test_threeDemo2():
    print("demo2_test.py -> test_threeDemo2")


@pytest.mark.skip
def test_fourthDemo2():
    print("demo2_test.py -> test_fourDemo2")
