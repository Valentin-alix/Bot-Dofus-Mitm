from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class RecycleResultMessage:
	def __init__(self, nuggetsForPrism:int, nuggetsForPlayer:int):
		self.nuggetsForPrism=nuggetsForPrism
		self.nuggetsForPlayer=nuggetsForPlayer