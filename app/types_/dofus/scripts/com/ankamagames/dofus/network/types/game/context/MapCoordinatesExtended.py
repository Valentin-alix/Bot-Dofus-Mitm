from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.MapCoordinatesAndId import MapCoordinatesAndId
if TYPE_CHECKING:
	...
class MapCoordinatesExtended(MapCoordinatesAndId):
	def __init__(self, subAreaId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.subAreaId=subAreaId