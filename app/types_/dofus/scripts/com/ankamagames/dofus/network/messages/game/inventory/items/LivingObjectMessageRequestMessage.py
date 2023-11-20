from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class LivingObjectMessageRequestMessage:
	def __init__(self, msgId:int, parameters:list[str], livingObject:int):
		self.msgId=msgId
		self.parameters=parameters
		self.livingObject=livingObject