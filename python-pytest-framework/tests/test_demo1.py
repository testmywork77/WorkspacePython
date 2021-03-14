import pytest


# pytest file should start with test_* or ends with *_test
# pytest method names should start with test_
# code should be wrapped in method only
@pytest.mark.smoke
def test_firstDemo1():
    print("test_demo1.py -> test_firstDemo1")


@pytest.mark.sanity
def test_secondDemo1():
    print("test_demo1.py -> test_secondDemo1")


@pytest.mark.regression
def test_thirdDemo1():
    print("test_demo1.py -> test_thirdDemo1")


@pytest.mark.skip
def test_fourthDemo1():
    print("test_demo1.py -> test_thirdDemo1")
