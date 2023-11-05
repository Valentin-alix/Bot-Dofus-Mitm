from pprint import pformat
from queue import Queue
from threading import Event
from typing import TypedDict


class ParsedMessage:
    def __init__(self, from_client: bool, __type__: str, **kwargs) -> None:
        self.from_client = from_client
        self.__type__ = __type__
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def __str__(self) -> str:
        return pformat(vars(self))


class ThreadsInfos(TypedDict):
    queue_handler_message: Queue[ParsedMessage]
    event_play_sniffer: Event
    event_close: Event


class SellerBuyerDescriptor(TypedDict):
    maxItemLevel: int
    maxItemPerAccount: int
    npcContextualId: int
    quantities: list[int]
    taxModificationPercentage: float
    taxPercentage: float
    types: list[int]
    unsoldDelay: int


class ObjectEffectInteger(TypedDict):
    actionId: int
    value: int


class BidExchangerObjectInfo(TypedDict):
    effects: list[ObjectEffectInteger]
    objectGID: int
    objectType: int
    objectUID: int
    prices: list[int]


# Messages from server


class ExchangeStartedBidBuyerMessage(ParsedMessage):
    """Received hdv infos"""

    buyerDescriptor: SellerBuyerDescriptor


class ExchangeTypesExchangerDescriptionForUserMessage(ParsedMessage):
    """Received hdv object types"""

    objectType: int
    typeDescription: list[int]


class ExchangeTypesItemsExchangerDescriptionForUserMessage(ParsedMessage):
    """Receivied hdv object prices"""

    itemTypeDescriptions: list[BidExchangerObjectInfo]
    objectGID: int
    objectType: int


# Messages from client


class ExchangeLeaveMessage(ParsedMessage):
    """When leaving modal"""

    dialogType: int
    success: bool


class ExchangeBidHouseSearchMessage(ParsedMessage):
    """When clicking object hdv"""

    follow: bool
    objectGID: int


#
class ExchangeBidHouseTypeMessage(ParsedMessage):
    """When checking category hdv"""

    follow: bool
    type: int
