import logging
import os
from datetime import datetime
from pathlib import Path

from app.gui.signals import AppSignals
from app.interfaces.models.common import BotInfo, ParsedMessage, ParsedMessageHandler
from app.utils.common import deep_dict_to_object, get_classes_in_path

logger = logging.getLogger(__name__)


class Handler:
    def __init__(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        self.bot_info = bot_info
        self.app_signals = app_signals
        self.types_handlers: list[type[ParsedMessageHandler]] = get_classes_in_path(
            os.path.join(Path(__file__).parent, "handlers"), "handler.py"
        )

    def handle_message_unpacked(self, json_msg: dict, from_client: bool):
        parsed_msg = ParsedMessage(**json_msg)
        if self.bot_info.sniffer_info.is_playing_event.is_set():
            self.app_signals.on_parsed_msg_info.emit(
                {
                    "parsed_msg": parsed_msg,
                    "from_client": from_client,
                    "time": datetime.now(),
                }
            )
        related_handler = next(
            (
                type_handler
                for type_handler in self.types_handlers
                if type_handler.__name__ == f"{parsed_msg.__type__}Handler"
            ),
            None,
        )
        if related_handler is not None:
            related_handler = related_handler(**vars(deep_dict_to_object(**json_msg)))
            related_handler.handle(self.bot_info, self.app_signals)
