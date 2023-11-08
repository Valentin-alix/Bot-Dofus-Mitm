from abc import abstractmethod

import types_
from network.parsed_message.parsed_message import ParsedMessage


class ParsedMessageServer(ParsedMessage):
    @abstractmethod
    def handle(self, threads_infos: types_.ThreadsInfos) -> None:
        ...
