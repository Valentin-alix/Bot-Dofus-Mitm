from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class PaginationRequestAbstractMessage:
	def __init__(self, offset:float, count:int):
		self.offset=offset
		self.count=count