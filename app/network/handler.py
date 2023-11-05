import logging
from blinker import signal
from copy import deepcopy
from modules.hdv import Hdv
from types_ import (
    ParsedMessage,
    DialogType,
    ExchangeLeaveMessage,
    ExchangeStartedBidBuyerMessage,
    ExchangeTypesExchangerDescriptionForUserMessage,
    ExchangeTypesItemsExchangerDescriptionForUserMessage,
    ThreadsInfos,
)

logger = logging.getLogger(__name__)


class Handler:
    hdv: Hdv | None = None

    def __init__(self, threads_infos: ThreadsInfos | None) -> None:
        self.threads_infos = threads_infos

    def handle_message_unpacked(self, parsed_message: ParsedMessage):
        if self.threads_infos is not None:
            self.threads_infos["queue_handler_message"].put(deepcopy(parsed_message))

        match parsed_message.__type__:
            case "ExchangeStartedBidBuyerMessage":
                parsed_message = ExchangeStartedBidBuyerMessage(**vars(parsed_message))
                self.hdv = Hdv(parsed_message.buyerDescriptor)
            case "ExchangeLeaveMessage":
                parsed_message = ExchangeLeaveMessage(**vars(parsed_message))
                if parsed_message.dialogType == DialogType.DIALOG_EXCHANGE:
                    self.hdv = None
            case "ExchangeTypesExchangerDescriptionForUserMessage":
                parsed_message = ExchangeTypesExchangerDescriptionForUserMessage(
                    **vars(parsed_message)
                )
                if self.hdv is not None:
                    self.hdv.on_received_opened_category(parsed_message)
            case "ExchangeTypesItemsExchangerDescriptionForUserMessage":
                parsed_message = ExchangeTypesItemsExchangerDescriptionForUserMessage(
                    **vars(parsed_message)
                )
                if self.hdv is not None:
                    self.hdv.on_receive_get_prices_gid(parsed_message)
            case "ExchangeCraftResultMagicWithObjectDescMessage":
                ...
            case "ExchangeObjectAddedMessage":
                ...
