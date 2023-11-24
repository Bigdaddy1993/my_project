import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("mylog.log", encoding="utf8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
