from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ExchangeSellMessage:
	def __init__(self, objectToSellId:int, quantity:int):
		self.objectToSellId=objectToSellId
		self.quantity=quantity