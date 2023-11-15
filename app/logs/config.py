import os
from pathlib import Path

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"simple": {"format": "%(asctime)s-%(levelname)s:%(message)s"}},
    "handlers": {
        "file_handler": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": os.path.join(Path(__file__).parent, "bot.log"),
            "mode": "+w",
        }
    },
    "loggers": {"root": {"handlers": ["file_handler"], "level": "INFO"}},
}
