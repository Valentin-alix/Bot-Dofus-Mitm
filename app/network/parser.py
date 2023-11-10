import logging
from typing import Callable

from network.handler import Handler
from network.models.message import Message
from types_ import ThreadsInfos, ParsedMessage

logger = logging.getLogger(__name__)


class MessageRawDataParser:
    def __init__(
        self,
        threads_infos: ThreadsInfos | None,
        on_error_callback: Callable | None = None,
    ) -> None:
        self.threads_infos = threads_infos
        self.on_error_callback = on_error_callback
        self.handler = (
            Handler(self.threads_infos) if self.threads_infos is not None else None
        )

    def parse(self, message: Message, from_client: bool) -> ParsedMessage | None:
        try:
            message_type = Message.get_message_type_from_id(message.id)
            logger.info(message_type)
            parsed_message = ParsedMessage(
                from_client, **Message.get_json_from_message(message_type, message.data)
            )
            if self.handler is not None:
                self.handler.handle_message_unpacked(parsed_message)
            return parsed_message
        except (KeyError, IndexError, UnicodeDecodeError) as err:
            if self.on_error_callback is not None:
                self.on_error_callback(err)
            return None
