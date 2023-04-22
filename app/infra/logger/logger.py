import logging
from app.domain.utils.logger.logger_interface import LoggerInterface
from app.main.config.settings import LOGGER_APP_NAME


class Logger(LoggerInterface):
    __instance = None

    @staticmethod
    def get_instance():
        if Logger.__instance is None:
            Logger.__instance = Logger()
        return Logger.__instance

    def __init__(self):
        print(LOGGER_APP_NAME)
        self.logger = logging.getLogger(LOGGER_APP_NAME)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s:%(levelname)s:%(name)s:%(module)s:%(funcName)s:%(lineno)s:%(message)s"
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def debug(self, message: str):
        self.logger.debug(message)

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message, exc_info=True)

    def critical(self, message: str):
        self.logger.critical(message)
