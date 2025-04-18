import os
from pathlib import Path

DIR = Path(__file__).resolve().parent.parent.parent
LOG_DIR = DIR / "resources/logs/"

# Ensure log directories exist
(LOG_DIR / "web").mkdir(parents=True, exist_ok=True)
(LOG_DIR / "bot").mkdir(parents=True, exist_ok=True)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {"format": "%(asctime)s | %(levelname)s | %(module)s | %(message)s"},
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "web_file": {
            "level": "INFO",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": os.path.join(LOG_DIR, "web", "web.log"),
            "when": "midnight",
            "backupCount": 30,
            "formatter": "verbose",
        },
        "bot_file": {
            "level": "INFO",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": os.path.join(LOG_DIR, "bot", "bot.log"),
            "when": "midnight",
            "backupCount": 30,
            "formatter": "verbose",
        },
    },
    "loggers": {
        "web": {
            "handlers": ["web_file", "console"],
            "level": "INFO",
            "propagate": True,
        },
        "bot": {
            "handlers": ["bot_file", "console"],
            "level": "INFO",
            "propagate": True,
        },
    },
}
