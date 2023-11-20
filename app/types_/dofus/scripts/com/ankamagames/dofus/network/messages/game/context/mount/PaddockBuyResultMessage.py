from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class PaddockBuyResultMessage:
	def __init__(self, paddockId:float, bought:bool, realPrice:int):
		self.paddockId=paddockId
		self.bought=bought
		self.realPrice=realPrice