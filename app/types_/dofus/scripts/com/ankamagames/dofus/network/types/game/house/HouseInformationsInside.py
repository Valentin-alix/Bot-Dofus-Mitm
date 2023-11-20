from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.house.HouseInformations import HouseInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.house.HouseInstanceInformations import HouseInstanceInformations
class HouseInformationsInside(HouseInformations):
	def __init__(self, houseInfos:HouseInstanceInformations, worldX:int, worldY:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.houseInfos=houseInfos
		self.worldX=worldX
		self.worldY=worldY