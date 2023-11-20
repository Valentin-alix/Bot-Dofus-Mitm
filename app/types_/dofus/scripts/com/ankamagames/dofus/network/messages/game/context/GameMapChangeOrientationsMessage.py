from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.ActorOrientation import ActorOrientation
class GameMapChangeOrientationsMessage:
	def __init__(self, orientations:list[ActorOrientation]):
		self.orientations=orientations