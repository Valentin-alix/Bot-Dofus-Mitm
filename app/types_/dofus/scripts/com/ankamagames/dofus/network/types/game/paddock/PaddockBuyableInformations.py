from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class PaddockBuyableInformations:
	def __init__(self, price:int, locked:bool):
		self.price=price
		self.locked=locked