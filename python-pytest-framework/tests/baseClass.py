import inspect
import logging


class BaseClass:
    def getLogger(self):
        logger_name = inspect.stack()[1][3]
        # logger = logging.getLogger(__name__)
        logger = logging.getLogger(logger_name)
        # Create FileHandler Object
        file_handler = logging.FileHandler("logFile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
        return logger
