from typing import TypedDict


class SelectedObject(TypedDict):
    quantity: int
    all_identical: bool
    object_gid: int
    object_uid: int
    minimal_prices: list[int]
    is_placed: bool


class OnSaleInfoWithLock(TypedDict):
    number: int
    sum_price: int
