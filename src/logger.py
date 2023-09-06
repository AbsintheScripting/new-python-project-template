"""Simple logger module"""

import logging


def logger_instance(
    logger_name: str,
    file_name: str = "logger.log"
) -> logging.Logger:
    """Creates a logger instance with the given name

    Args:
        logger_name (str): You can use `__name__` for example
        file_name (str, optional): Filename for the logs. Defaults to "logger.log".

    Returns:
        logging.Logger: Python logger with my settings
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(file_name)
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    formatter = logging.Formatter(
        '[%(asctime)s][%(name)s][%(levelname)s]: %(message)s'
    )
    file_handler.setFormatter(formatter)
    return logger
