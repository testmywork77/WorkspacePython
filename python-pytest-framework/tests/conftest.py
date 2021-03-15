import pytest


@pytest.fixture()
def setup():
    print("SetUp fixture - Before test")
    yield
    print("TearDown fixture - After test")


# This fixture allows only at class level
@pytest.fixture(scope="class")
def init():
    print("Execute before all tests")
    yield
    print("Execute after all tests")


@pytest.fixture()
def data_calculator():
    return [4, 2]


@pytest.fixture(params=[(4, 2), (8, 6), (12, 6)])
def data_parameterized(request):
    return request.param


@pytest.fixture(params=["chrome", "firefox", "edge"])
def cross_browser(request):
    return request.param


@pytest.fixture(params=[(1, "Name1", "Loc1", "Name1@gmail.com"),
                        (2, "Name2", "Loc2", "Name2@gmail.com"), (3, "Name3", "Loc3", "Name3@gmail.com")])
def data_employee(request):
    return request.param
