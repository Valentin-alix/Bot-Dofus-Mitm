import logging
from network.models.message import Message
import pprint

logger = logging.getLogger(__name__)


def handle_message_unpacked(msg: Message):
    logger.info(msg.message_type)
    # logger.info(f"{msg.message_type} :\n{pprint.pformat(msg.content)}")
    if msg.message_type == "ExchangeCraftResultMagicWithObjectDescMessage":
        print(msg.content)
    elif msg.message_type == "ExchangeObjectAddedMessage":
        print(msg.content)
