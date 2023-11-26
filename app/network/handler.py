import logging
import os
from datetime import datetime
from pathlib import Path

from app.gui.signals import AppSignals
from app.network.utils import deep_dict_to_object, get_classes_in_path
from app.types_.models.common import BotInfo, ParsedMessageHandler, ParsedMessage

logger = logging.getLogger(__name__)


class Handler:
    def __init__(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        self.bot_info = bot_info
        self.app_signals = app_signals
        self.classes_handler = get_classes_in_path(
            os.path.join(Path(__file__).parent, "handlers"), "handler.py"
        )

    def handle_message_unpacked(self, json_msg: dict, from_client: bool):
        parsed_msg = ParsedMessage(**json_msg)
        if self.bot_info.sniffer_info.is_playing_event.is_set():
            self.app_signals.on_parsed_msg_info.emit(
                {"parsed_msg": parsed_msg, "from_client": from_client, "time": datetime.now()})
        class_handler = next(
            (
                class_handler
                for class_handler in self.classes_handler
                if class_handler.__name__ == f"{parsed_msg.__type__}Handler"
            ),
            None,
        )
        if class_handler is not None:
            class_instance = deep_dict_to_object(**json_msg)
            class_handler = class_handler(**vars(class_instance))
            assert isinstance(class_handler, ParsedMessageHandler)
            class_handler.handle(self.bot_info, self.app_signals)
