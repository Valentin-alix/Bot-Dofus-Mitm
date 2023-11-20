from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class TeleportPlayerOfferMessage:
	def __init__(self, mapId:float, message:str, timeLeft:int, requesterId:int):
		self.mapId=mapId
		self.message=message
		self.timeLeft=timeLeft
		self.requesterId=requesterId