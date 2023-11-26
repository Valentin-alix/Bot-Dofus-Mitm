from typing import TypedDict, NotRequired


class SelectedObject(TypedDict):
    object_gid: int
    is_placed: bool
    minimal_prices: NotRequired[list[int]]


class TreatedObjectProgression(TypedDict):
    total_objects_count: int
    treated_objects_count: int
