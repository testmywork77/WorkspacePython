# Sample Test methods
import pytest


class TestSample:
    @pytest.mark.smoke
    def test_smoke(self):
        print('test_smoke')

    @pytest.mark.sanity
    def test_sanity(self):
        print('test_sanity')

    @pytest.mark.regression
    def test_regression(self):
        print('test_regression')

    @pytest.mark.smoke
    @pytest.mark.sanity
    def test_smoke_sanity(self):
        print('test_smoke_sanity')

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_smoke_regression(self):
        print('test_smoke_regression')

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_sanity_regression(self):
        print('test_sanity_regression')
