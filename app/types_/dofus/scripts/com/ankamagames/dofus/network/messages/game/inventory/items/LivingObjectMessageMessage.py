from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class LivingObjectMessageMessage:
	def __init__(self, msgId:int, timeStamp:int, owner:str, objectGenericId:int):
		self.msgId=msgId
		self.timeStamp=timeStamp
		self.owner=owner
		self.objectGenericId=objectGenericId