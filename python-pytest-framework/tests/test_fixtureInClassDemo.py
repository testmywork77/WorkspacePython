import pytest


@pytest.mark.usefixtures('setup')
class TestFixtureInClassDemo:
    def test_fixtureDemo1(self):
        print("test_fixtureDemo")

    def test_fixtureDemo2(self):
        print("test_fixtureDemo")

    def test_fixtureDemo3(self):
        print("test_fixtureDemo")
