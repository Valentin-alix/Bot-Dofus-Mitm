from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.EntityMovementInformations import EntityMovementInformations
class GameContextMoveElementMessage:
	def __init__(self, movement:EntityMovementInformations):
		self.movement=movement