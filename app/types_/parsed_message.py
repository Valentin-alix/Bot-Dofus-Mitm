from abc import abstractmethod
from pprint import pformat

from app.types_.interface import BotInfo


class ParsedMessage:
    def __init__(self, from_client: bool, __type__: str, **kwargs) -> None:
        self.from_client = from_client
        self.__type__ = __type__
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def __str__(self) -> str:
        return pformat(vars(self))


class ParsedMessageHandler:
    @abstractmethod
    def handle(self, bot_info: BotInfo) -> None:
        ...
