from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.alteration.AlterationInfo import AlterationInfo
class AlterationsUpdatedMessage:
	def __init__(self, alterations:list[AlterationInfo]):
		self.alterations=alterations