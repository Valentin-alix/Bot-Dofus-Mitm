from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage
if TYPE_CHECKING:
	...
class MapComplementaryInformationsWithCoordsMessage(MapComplementaryInformationsDataMessage):
	def __init__(self, worldX:int, worldY:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.worldX=worldX
		self.worldY=worldY