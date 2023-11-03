from network.models.message import ParsedMessage
from typing import TypedDict


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


# Messages
class ExchangeStartedBidBuyerMessage(ParsedMessage):
    buyerDescriptor: SellerBuyerDescriptor


class ExchangeTypesExchangerDescriptionForUserMessage(ParsedMessage):
    objectType: int
    typeDescription: list[int]


class ExchangeTypesItemsExchangerDescriptionForUserMessage(ParsedMessage):
    itemTypeDescriptions: list[BidExchangerObjectInfo]
    objectGID: int
    objectType: int
