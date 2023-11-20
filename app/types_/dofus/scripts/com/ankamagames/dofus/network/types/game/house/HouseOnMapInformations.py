from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.house.HouseInformations import HouseInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.house.HouseInstanceInformations import HouseInstanceInformations
class HouseOnMapInformations(HouseInformations):
	def __init__(self, doorsOnMap:list[int], houseInstances:list[HouseInstanceInformations], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.doorsOnMap=doorsOnMap
		self.houseInstances=houseInstances