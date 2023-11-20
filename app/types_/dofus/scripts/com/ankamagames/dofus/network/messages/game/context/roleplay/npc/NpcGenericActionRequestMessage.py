from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class NpcGenericActionRequestMessage:
	def __init__(self, npcId:int, npcActionId:int, npcMapId:float):
		self.npcId=npcId
		self.npcActionId=npcActionId
		self.npcMapId=npcMapId