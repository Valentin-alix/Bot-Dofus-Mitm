from typing import TypedDict


class SelectedObject(TypedDict):
    object_gid: int
    minimal_prices: list[int]
    is_placed: bool


class OnSaleInfoWithLock(TypedDict):
    number: int
    sum_price: int
