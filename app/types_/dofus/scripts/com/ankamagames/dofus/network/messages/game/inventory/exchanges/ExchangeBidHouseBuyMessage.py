from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ExchangeBidHouseBuyMessage:
	def __init__(self, uid:int, qty:int, price:int):
		self.uid=uid
		self.qty=qty
		self.price=price