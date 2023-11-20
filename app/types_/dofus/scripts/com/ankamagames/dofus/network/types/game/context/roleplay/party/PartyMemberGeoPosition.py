from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class PartyMemberGeoPosition:
	def __init__(self, memberId:int, worldX:int, worldY:int, mapId:float, subAreaId:int):
		self.memberId=memberId
		self.worldX=worldX
		self.worldY=worldY
		self.mapId=mapId
		self.subAreaId=subAreaId