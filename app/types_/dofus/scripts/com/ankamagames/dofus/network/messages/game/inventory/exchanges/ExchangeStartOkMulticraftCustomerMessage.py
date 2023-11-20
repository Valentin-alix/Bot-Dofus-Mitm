from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ExchangeStartOkMulticraftCustomerMessage:
	def __init__(self, skillId:int, crafterJobLevel:int):
		self.skillId=skillId
		self.crafterJobLevel=crafterJobLevel