import os
import logging
from .config import settings


def setup_logger(service):
    logger = logging.getLogger(service)
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(os.path.join(settings.path_root, 'logs', f"{service}.log"))
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s at %(lineno)d in %(funcName)s: %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
