from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.ActorOrientation import ActorOrientation
class GameMapChangeOrientationMessage:
	def __init__(self, orientation:ActorOrientation):
		self.orientation=orientation