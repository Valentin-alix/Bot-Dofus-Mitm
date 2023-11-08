from __future__ import annotations
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


class ObjectItemToSellInBid(TypedDict):
    effects: list
    objectGID: int
    objectPrice: int
    objectUID: int
    quantity: int
    unsoldDelay: int


class ObjectEffect(TypedDict):
    actionId: int


class ObjectItem(TypedDict):
    objectGID: int
    effects: list[ObjectEffect]
    objectUID: int
    quantity: int
