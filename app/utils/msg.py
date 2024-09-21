import logging
from queue import Queue

logger = logging.getLogger(__name__)


def send_parsed_msg(message_to_send_queue: Queue[dict], parsed_message):
    logger.info(f"Sending: {parsed_message.__class__.__name__}")
    msg_to_send = {
        **vars(parsed_message),
        "__type__": parsed_message.__class__.__name__,
    }
    message_to_send_queue.put(msg_to_send)
