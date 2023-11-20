from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.MapCoordinates import MapCoordinates
class CompassUpdateMessage:
	def __init__(self, type:int, coords:MapCoordinates):
		self.type=type
		self.coords=coords