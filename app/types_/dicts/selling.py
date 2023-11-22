from typing import TypedDict, NotRequired


class SelectedObject(TypedDict):
    object_gid: int
    is_placed: bool
    minimal_prices: NotRequired[list[int]]


class OnSaleInfoWithLock(TypedDict):
    number: int
    sum_price: int
