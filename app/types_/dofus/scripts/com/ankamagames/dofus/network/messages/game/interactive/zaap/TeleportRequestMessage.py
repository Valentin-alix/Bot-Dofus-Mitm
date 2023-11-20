from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class TeleportRequestMessage:
	def __init__(self, sourceType:int, destinationType:int, mapId:float):
		self.sourceType=sourceType
		self.destinationType=destinationType
		self.mapId=mapId