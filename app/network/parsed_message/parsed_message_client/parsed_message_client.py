import logging

from network.parsed_message.parsed_message import ParsedMessage
from types_ import ThreadsInfos

logger = logging.getLogger(__name__)


class ParsedMessageClient(ParsedMessage):
    def send(self, threads_infos: ThreadsInfos) -> None:
        logger.info(f"Sending {self.__type__}")
        threads_infos.get("queue_msg_to_send").put(vars(self))
