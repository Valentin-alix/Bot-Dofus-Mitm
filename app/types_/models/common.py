from abc import abstractmethod
from dataclasses import dataclass, field
from pprint import pformat
from queue import Queue

from app.gui.signals import AppSignals
from app.modules.character import Character
from app.types_.models.fm import FmInfo
from app.types_.models.scraping import ScrapingInfo
from app.types_.models.selling import SellingInfo
from app.types_.models.sniffer import SnifferInfo


@dataclass
class CommonInfo:
    message_to_send_queue: Queue[dict] = Queue()
    server_id: int | None = None
    character: Character | None = None


@dataclass
class BotInfo:
    common_info: CommonInfo = field(default_factory=CommonInfo)
    sniffer_info: SnifferInfo = field(default_factory=SnifferInfo)
    scraping_info: ScrapingInfo = field(default_factory=ScrapingInfo)
    fm_info: FmInfo = field(default_factory=FmInfo)
    selling_info: SellingInfo = field(default_factory=SellingInfo)


class ParsedMessageHandler:
    @abstractmethod
    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        ...


class ParsedMessage:
    def __init__(self, __type__: str, **kwargs) -> None:
        self.__type__ = __type__
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def __str__(self) -> str:
        return pformat(vars(self))
