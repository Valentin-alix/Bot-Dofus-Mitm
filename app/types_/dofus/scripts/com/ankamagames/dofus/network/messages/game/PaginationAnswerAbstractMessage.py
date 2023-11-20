from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class PaginationAnswerAbstractMessage:
	def __init__(self, offset:float, count:int, total:int):
		self.offset=offset
		self.count=count
		self.total=total