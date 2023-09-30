import logging

LOGGER_OBJ = None

logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler("logs.log")
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

LOGGER_OBJ = logger
