from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.alteration.AlterationInfo import AlterationInfo
class AlterationRemovedMessage:
	def __init__(self, alteration:AlterationInfo):
		self.alteration=alteration