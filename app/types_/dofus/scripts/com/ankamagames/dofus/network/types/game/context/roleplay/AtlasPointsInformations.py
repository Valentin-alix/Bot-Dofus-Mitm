from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.MapCoordinatesExtended import MapCoordinatesExtended
class AtlasPointsInformations:
	def __init__(self, type:int, coords:list[MapCoordinatesExtended]):
		self.type=type
		self.coords=coords