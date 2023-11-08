from __future__ import annotations

import logging
from network.parsed_message.parsed_message import ParsedMessage
import types_

logger = logging.getLogger(__name__)


class ParsedMessageClient(ParsedMessage):
    def send(self, threads_infos: types_.ThreadsInfos) -> None:
        logger.info(f"Sending {self.__type__}")
        threads_infos.get("queue_msg_to_send").put(vars(self))
