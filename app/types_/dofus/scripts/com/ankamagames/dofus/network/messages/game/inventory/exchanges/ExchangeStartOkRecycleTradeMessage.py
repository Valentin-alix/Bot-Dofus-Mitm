from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ExchangeStartOkRecycleTradeMessage:
	def __init__(self, percentToPrism:int, percentToPlayer:int, adjacentSubareaPossessed:list[int], adjacentSubareaUnpossessed:list[int]):
		self.percentToPrism=percentToPrism
		self.percentToPlayer=percentToPlayer
		self.adjacentSubareaPossessed=adjacentSubareaPossessed
		self.adjacentSubareaUnpossessed=adjacentSubareaUnpossessed