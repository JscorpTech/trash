import logging
import logging.config
from config.conf.logs import LOGGING

logging.config.dictConfig(LOGGING)


logger = logging.getLogger("web")
