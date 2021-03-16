from tests.baseClass import BaseClass


class TestLogger(BaseClass):
    def test_LoggerDemo1(self):
        log = self.getLogger()
        log.debug("Debug message")
        log.info("Info message")
