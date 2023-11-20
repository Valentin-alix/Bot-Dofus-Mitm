from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.BasicAllianceInformations import BasicAllianceInformations
class TaxCollectorAttackedMessage:
	def __init__(self, firstNameId:int, lastNameId:int, worldX:int, worldY:int, mapId:float, subAreaId:int, alliance:BasicAllianceInformations):
		self.firstNameId=firstNameId
		self.lastNameId=lastNameId
		self.worldX=worldX
		self.worldY=worldY
		self.mapId=mapId
		self.subAreaId=subAreaId
		self.alliance=alliance