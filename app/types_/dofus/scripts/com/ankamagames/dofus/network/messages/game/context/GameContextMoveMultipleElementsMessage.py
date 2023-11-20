from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.EntityMovementInformations import EntityMovementInformations
class GameContextMoveMultipleElementsMessage:
	def __init__(self, movements:list[EntityMovementInformations]):
		self.movements=movements