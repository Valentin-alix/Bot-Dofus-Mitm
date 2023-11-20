from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class TaxCollectorBasicInformations:
	def __init__(self, firstNameId:int, lastNameId:int, worldX:int, worldY:int, mapId:float, subAreaId:int):
		self.firstNameId=firstNameId
		self.lastNameId=lastNameId
		self.worldX=worldX
		self.worldY=worldY
		self.mapId=mapId
		self.subAreaId=subAreaId