from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.house.HouseInformations import HouseInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.house.HouseInstanceInformations import HouseInstanceInformations
class AccountHouseInformations(HouseInformations):
	def __init__(self, houseInfos:HouseInstanceInformations, worldX:int, worldY:int, mapId:float, subAreaId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.houseInfos=houseInfos
		self.worldX=worldX
		self.worldY=worldY
		self.mapId=mapId
		self.subAreaId=subAreaId