from utilities.BaseClass import BaseClass


class TestCalculator(BaseClass):
    def test_addition(self):
        log = self.getLogger()
        log.info("Test Addition-Begin")
        result = 2 + 4
        assert 6 == result
        log.info("Test Addition-End")
