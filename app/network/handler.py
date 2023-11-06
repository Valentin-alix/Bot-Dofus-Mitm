import logging
from threading import Timer
from typing import Type
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
from types_.constants import GAME_SERVER

logger = logging.getLogger(__name__)


class Handler:
    def __init__(self, threads_infos: ThreadsInfos | None) -> None:
        self.hdv: Hdv | None = None
        self.threads_infos = threads_infos

    def handle_message_unpacked(self, parsed_message: ParsedMessage):
        if self.threads_infos is not None:
            self.threads_infos.get("queue_handler_message").put(parsed_message)

            if self.threads_infos.get("event_connected").is_set():
                match parsed_message.__type__:
                    case "ExchangeStartedBidBuyerMessage":
                        parsed_message = ExchangeStartedBidBuyerMessage(
                            **vars(parsed_message)
                        )
                        self.hdv = Hdv(
                            parsed_message.buyerDescriptor,
                            threads_infos=self.threads_infos,
                        )
                    case "ExchangeLeaveMessage":
                        parsed_message = ExchangeLeaveMessage(**vars(parsed_message))
                        if parsed_message.dialogType == DialogType.DIALOG_EXCHANGE:
                            self.threads_infos["queue_current_hdv"].put(None)
                            self.hdv = None
                    case "ExchangeTypesExchangerDescriptionForUserMessage":
                        parsed_message = (
                            ExchangeTypesExchangerDescriptionForUserMessage(
                                **vars(parsed_message)
                            )
                        )
                        if (
                            self.threads_infos.get("event_play_hdv").is_set()
                            and self.hdv is not None
                        ):
                            self.hdv.on_received_checked_category(parsed_message)
                    case "ExchangeTypesItemsExchangerDescriptionForUserMessage":
                        parsed_message = (
                            ExchangeTypesItemsExchangerDescriptionForUserMessage(
                                **vars(parsed_message)
                            )
                        )
                        if (
                            self.threads_infos.get("event_play_hdv").is_set()
                            and self.hdv is not None
                        ):
                            self.hdv.on_receive_get_prices_gid(parsed_message)
                    case "ExchangeCraftResultMagicWithObjectDescMessage":
                        ...
                    case "ExchangeObjectAddedMessage":
                        ...
