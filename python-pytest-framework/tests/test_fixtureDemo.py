import pytest

# moved to conftest.py
# @pytest.fixture()
# def setup():
#     print("Setup fixture - Before test")
#     yield
#     print("TearDown fixture - After test")


def test_fixtureDemo(setup):
    print("test_fixtureDemo")
