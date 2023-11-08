from __future__ import annotations

from abc import abstractmethod
from network.parsed_message.parsed_message import ParsedMessage

import types_


class ParsedMessageServer(ParsedMessage):
    @abstractmethod
    def handle(self, threads_infos: types_.ThreadsInfos) -> None:
        ...
