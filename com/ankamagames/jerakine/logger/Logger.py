import logging
from com.ankamagames.jerakine.metaclasses.Singleton import Singleton
import datetime
import os


class Logger(logging.Logger):
    _logger = None

    def __init__(self, log_prefix=""):
        super().__init__("logger")
        self._prefix = log_prefix
        self.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s | %(filename)s:%(lineno)s] > %(message)s"
        )

        now = datetime.datetime.now()
        dirname = "./log"

        if not os.path.isdir(dirname):
            os.mkdir(dirname)
        fileHandler = logging.FileHandler(
            dirname + f"/log_{self._prefix}" + now.strftime("%Y-%m-%d") + ".log"
        )

        streamHandler = logging.StreamHandler()

        fileHandler.setFormatter(formatter)
        streamHandler.setFormatter(formatter)

        self.addHandler(fileHandler)
        self.addHandler(streamHandler)

    def get_logger(self):
        return self
