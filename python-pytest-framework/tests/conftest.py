import pytest


@pytest.fixture()
def setup():
    print("SetUp fixture - Before test")
    yield
    print("TearDown fixture - After test")


@pytest.fixture(scope="class")
def init():
    print("Execute before all tests")
    yield
    print("Execute after all tests")
