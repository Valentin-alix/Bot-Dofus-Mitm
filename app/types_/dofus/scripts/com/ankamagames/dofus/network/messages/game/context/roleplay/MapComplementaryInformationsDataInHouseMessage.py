from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.house.HouseInformationsInside import HouseInformationsInside
class MapComplementaryInformationsDataInHouseMessage(MapComplementaryInformationsDataMessage):
	def __init__(self, currentHouse:HouseInformationsInside, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.currentHouse=currentHouse