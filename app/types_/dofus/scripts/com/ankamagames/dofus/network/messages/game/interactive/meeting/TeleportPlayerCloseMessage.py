from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class TeleportPlayerCloseMessage:
	def __init__(self, mapId:float, requesterId:int):
		self.mapId=mapId
		self.requesterId=requesterId