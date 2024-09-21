from abc import abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from pprint import pformat
from queue import Queue

from app.gui.signals import AppSignals
from app.interfaces.models.scrapping import ScrappingInfo
from app.interfaces.models.selling import SellingInfo
from app.interfaces.models.sniffer import SnifferInfo
from app.modules.character import Character


@dataclass
class CommonInfo:
    message_to_send_queue: Queue[dict] = Queue()
    server_id: int | None = None
    subscription_end_date: datetime | None = None
    character: Character | None = None


@dataclass
class BotInfo:
    common_info: CommonInfo = field(default_factory=CommonInfo)
    sniffer_info: SnifferInfo = field(default_factory=SnifferInfo)
    scraping_info: ScrappingInfo = field(default_factory=ScrappingInfo)
    selling_info: SellingInfo = field(default_factory=SellingInfo)


class ParsedMessageHandler:
    @abstractmethod
    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None: ...


class ParsedMessage:
    def __init__(self, __type__: str, **kwargs) -> None:
        self.__type__ = __type__
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def __str__(self) -> str:
        return pformat(vars(self))
