import pytest


@pytest.mark.usefixtures("init")
class TestFixtureAtClassScopeDemo:
    def test_fixtureDemo1(self):
        print("test_fixtureDemo")

    def test_fixtureDemo2(self):
        print("test_fixtureDemo")

    def test_fixtureDemo3(self):
        print("test_fixtureDemo")
