import logging

from models.data import Data

logger = logging.getLogger(__name__)


class ExchangeObjectAddedMessage:
    @staticmethod
    def deserialize(data: Data):
        return None

    def on_receive(message):
        logger.info(message)
