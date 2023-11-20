from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ExchangeBuyMessage:
	def __init__(self, objectToBuyId:int, quantity:int):
		self.objectToBuyId=objectToBuyId
		self.quantity=quantity