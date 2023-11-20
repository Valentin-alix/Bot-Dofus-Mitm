from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ExchangeHandleMountsMessage:
	def __init__(self, actionType:int, ridesId:list[int]):
		self.actionType=actionType
		self.ridesId=ridesId