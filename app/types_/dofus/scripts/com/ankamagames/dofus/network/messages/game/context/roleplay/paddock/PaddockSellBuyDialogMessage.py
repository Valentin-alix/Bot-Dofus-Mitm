from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class PaddockSellBuyDialogMessage:
	def __init__(self, bsell:bool, ownerId:int, price:int):
		self.bsell=bsell
		self.ownerId=ownerId
		self.price=price