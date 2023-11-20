from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.prism.PrismInformation import PrismInformation
class PrismGeolocalizedInformation:
	def __init__(self, subAreaId:int, allianceId:int, worldX:int, worldY:int, mapId:float, prism:PrismInformation):
		self.subAreaId=subAreaId
		self.allianceId=allianceId
		self.worldX=worldX
		self.worldY=worldY
		self.mapId=mapId
		self.prism=prism