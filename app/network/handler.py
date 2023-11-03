import logging
import pprint

from network.models.message import ParsedMessage

logger = logging.getLogger(__name__)


def handle_message_unpacked(msg: ParsedMessage):
    # logger.info(msg.__type__)
    # logger.info(f"{msg.message_type} :\n{pprint.pformat(msg.content)}")
    if msg.__type__ == "ExchangeTypesItemsExchangerDescriptionForUserMessage":
        print(msg)
    elif msg.__type__ == "ExchangeCraftResultMagicWithObjectDescMessage":
        print(msg)
    elif msg.__type__ == "ExchangeObjectAddedMessage":
        print(msg)
