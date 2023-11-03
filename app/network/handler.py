import json
import logging
import os
from pathlib import Path
import pprint
from time import perf_counter

from network.models.message import ParsedMessage
from network.models.parsed_messages import (
    ExchangeStartedBidBuyerMessage,
    ExchangeTypesExchangerDescriptionForUserMessage,
    ExchangeTypesItemsExchangerDescriptionForUserMessage,
)

logger = logging.getLogger(__name__)


class Handler:
    def __init__(self) -> None:
        d2o_item_file_path = os.path.join(
            Path(__file__).parent.parent, "PyDofus", "output", "d2o", "Items.json"
        )
        with open(d2o_item_file_path, encoding="utf8") as d2o_file:
            self.d2o_items = json.load(d2o_file)

        d2i_file_path = os.path.join(
            Path(__file__).parent.parent, "PyDofus", "output", "i18n_fr.json"
        )
        with open(d2i_file_path, encoding="utf8") as d2i_file:
            self.d2i_texts = json.load(d2i_file)["texts"]

    def get_name_by_id(self, _id: int) -> str:
        name_id = next(
            item for item in self.d2o_items if item.get("id", None) == _id
        ).get("nameId")
        name = self.d2i_texts.get(str(name_id))
        return name

    def handle_message_unpacked(self, msg: ParsedMessage):
        match msg.__type__:
            case "ExchangeStartedBidBuyerMessage":
                # Received hdv categories
                msg = ExchangeStartedBidBuyerMessage(**vars(msg))
                # print(msg.buyerDescriptor)
            case "ExchangeTypesExchangerDescriptionForUserMessage":
                # Received hdv item categories
                msg = ExchangeTypesExchangerDescriptionForUserMessage(**vars(msg))
                # print(msg.typeDescription)
            case "ExchangeTypesItemsExchangerDescriptionForUserMessage":
                msg = ExchangeTypesItemsExchangerDescriptionForUserMessage(**vars(msg))
                print(self.get_name_by_id(msg.objectGID))
                for elem in msg.itemTypeDescriptions:
                    print(elem.get("prices"))
            case "ExchangeCraftResultMagicWithObjectDescMessage":
                print(msg)
            case "ExchangeObjectAddedMessage":
                print(msg)
