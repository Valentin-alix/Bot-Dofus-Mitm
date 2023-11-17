import logging
from typing import Callable

from app.network.handler import Handler
from app.types_ import ParsedMessage, BotInfo
from app.types_.models.message import Message

logger = logging.getLogger(__name__)


class MessageRawDataParser:
    def __init__(
            self,
            bot_info: BotInfo | None,
            on_error_callback: Callable | None = None,
    ) -> None:
        self.bot_info = bot_info
        self.on_error_callback = on_error_callback
        self.handler = Handler(self.bot_info) if self.bot_info is not None else None

    def parse(self, message: Message, from_client: bool):
        try:
            message_type = Message.get_message_type_from_id(message.id)
            logger.info(message_type)

            parsed_message = ParsedMessage(
                from_client, **Message.get_json_from_message(message_type, message.data)
            )
            if self.handler is not None:
                self.handler.handle_message_unpacked(parsed_message)
        except (KeyError, IndexError, UnicodeDecodeError) as err:
            if self.on_error_callback is not None:
                self.on_error_callback(err)
            return None
