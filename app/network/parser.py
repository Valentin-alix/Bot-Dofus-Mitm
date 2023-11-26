import json
import logging
from pathlib import Path
from typing import Callable

from app.gui.signals import AppSignals
from app.network.handler import Handler
from app.types_.models.common import BotInfo
from app.types_.models.network.message import Message

logger = logging.getLogger(__name__)


class MessageRawDataParser:
    def __init__(
            self,
            bot_info: BotInfo | None,
            app_signals: AppSignals,
            on_error_callback: Callable | None = None,
    ) -> None:
        self.bot_info = bot_info
        self.app_signals = app_signals
        self.on_error_callback = on_error_callback
        self.handler = Handler(self.bot_info, self.app_signals) if self.bot_info is not None else None

    def parse(self, message: Message, from_client: bool):
        try:
            message_type = Message.get_message_type_from_id(message.id)
            logger.info(message_type)
            json_msg = Message.get_json_from_message(message_type, message.data)
            if self.handler is not None:
                self.handler.handle_message_unpacked(json_msg, from_client)
        except (KeyError, IndexError, UnicodeDecodeError) as err:
            if self.on_error_callback is not None:
                self.on_error_callback(err)
