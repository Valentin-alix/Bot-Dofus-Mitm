from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.interactive.MapObstacle import MapObstacle
class MapObstacleUpdateMessage:
	def __init__(self, obstacles:list[MapObstacle]):
		self.obstacles=obstacles