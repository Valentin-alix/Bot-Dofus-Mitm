from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class EntityTalkMessage:
	def __init__(self, entityId:float, textId:int, parameters:list[str]):
		self.entityId=entityId
		self.textId=textId
		self.parameters=parameters