from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class NpcDialogCreationMessage:
	def __init__(self, mapId:float, npcId:int):
		self.mapId=mapId
		self.npcId=npcId