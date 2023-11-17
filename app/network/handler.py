import logging
import os
from pathlib import Path

from app.modules.character import Character
from app.modules.hdv.buying_hdv import BuyingHdv
from app.modules.hdv.selling_hdv import SellingHdv
from app.network.utils import deep_dict_to_object, get_classes_in_path
from app.types_ import ParsedMessageHandler, BotInfo, ParsedMessage

logger = logging.getLogger(__name__)


class Handler:
    def __init__(self, bot_info: BotInfo) -> None:
        self.buying_hdv: BuyingHdv | None = None
        self.selling_hdv: SellingHdv | None = None
        self.character: Character | None = None
        self.bot_info = bot_info
        self.classes_handler = get_classes_in_path(
            os.path.join(Path(__file__).parent, "handlers"), "handler.py"
        )

    def handle_message_unpacked(self, parsed_message: ParsedMessage):
        if self.bot_info.sniffer_info.is_playing_event.is_set():
            self.bot_info.sniffer_info.parsed_message_queue.put(parsed_message)
        class_handler = next(
            (
                class_handler
                for class_handler in self.classes_handler
                if class_handler.__name__ == f"{parsed_message.__type__}Handler"
            ),
            None,
        )
        if class_handler is not None:
            class_instance = deep_dict_to_object(**vars(parsed_message))
            class_handler = class_handler(**vars(class_instance))
            if isinstance(class_handler, ParsedMessageHandler):
                class_handler.handle(self.bot_info)
            else:
                raise ValueError("class handler is not of type ParsedMessageHandler")
