from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GroupTeleportPlayerOfferMessage:
	def __init__(self, mapId:float, worldX:int, worldY:int, timeLeft:int, requesterId:int, requesterName:str):
		self.mapId=mapId
		self.worldX=worldX
		self.worldY=worldY
		self.timeLeft=timeLeft
		self.requesterId=requesterId
		self.requesterName=requesterName