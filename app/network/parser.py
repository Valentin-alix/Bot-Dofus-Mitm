import logging
from queue import Queue
from typing import Callable

from network.handler import handle_message_unpacked
from network.models.message import Message, ParsedMessage

logger = logging.getLogger(__name__)


class MessageRawDataParser:
    queue_handler_message: Queue[ParsedMessage] | None = None
    on_error_callback: Callable | None = None

    def __init__(
        self,
        queue_handler_message: Queue[ParsedMessage] | None = None,
        on_error_callback: Callable | None = None,
    ) -> None:
        self.queue_handler_message = queue_handler_message
        self.on_error_callback = on_error_callback

    def parse(self, message: Message, from_client: bool) -> ParsedMessage | None:
        try:
            message_type = Message.get_message_type_from_id(message.id)
            parsed_message = ParsedMessage(
                from_client, **Message.get_json_from_message(message_type, message.data)
            )
            if self.queue_handler_message is not None:
                self.queue_handler_message.put(parsed_message)
            handle_message_unpacked(parsed_message)
            return parsed_message

        except (KeyError, IndexError) as err:
            if self.on_error_callback is not None:
                self.on_error_callback(err)
            logger.error(f"Could not parse {message.id}")
            return None
