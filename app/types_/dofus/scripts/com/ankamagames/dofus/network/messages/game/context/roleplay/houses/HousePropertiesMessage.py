from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.house.HouseInstanceInformations import HouseInstanceInformations
class HousePropertiesMessage:
	def __init__(self, houseId:int, doorsOnMap:list[int], properties:HouseInstanceInformations):
		self.houseId=houseId
		self.doorsOnMap=doorsOnMap
		self.properties=properties