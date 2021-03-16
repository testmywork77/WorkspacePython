import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)
    # Create FileHandler Object
    file_handler = logging.FileHandler("logFile.log")
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    # logger.setLevel(logging.DEBUG)
    logger.setLevel(logging.INFO)
    logger.debug("A debug statement")
    logger.info("A info statement")
    logger.warning("A warning statement")
    logger.error("A error statement")
    logger.critical("A critical statement")
