from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ExchangeObjectMoveToTabMessage:
	def __init__(self, objectUID:int, quantity:int, tabNumber:int):
		self.objectUID=objectUID
		self.quantity=quantity
		self.tabNumber=tabNumber