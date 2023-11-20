from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ExchangeTypesExchangerDescriptionForUserMessage:
	def __init__(self, objectType:int, typeDescription:list[int]):
		self.objectType=objectType
		self.typeDescription=typeDescription