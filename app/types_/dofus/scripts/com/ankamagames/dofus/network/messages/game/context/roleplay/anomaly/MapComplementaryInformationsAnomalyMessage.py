from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage
if TYPE_CHECKING:
	...
class MapComplementaryInformationsAnomalyMessage(MapComplementaryInformationsDataMessage):
	def __init__(self, level:int, closingTime:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.level=level
		self.closingTime=closingTime