from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.MapCoordinates import MapCoordinates
if TYPE_CHECKING:
	...
class MapCoordinatesAndId(MapCoordinates):
	def __init__(self, mapId:float, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.mapId=mapId