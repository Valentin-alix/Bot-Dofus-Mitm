from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameContextRemoveMultipleElementsMessage:
	def __init__(self, elementsIds:list[float]):
		self.elementsIds=elementsIds