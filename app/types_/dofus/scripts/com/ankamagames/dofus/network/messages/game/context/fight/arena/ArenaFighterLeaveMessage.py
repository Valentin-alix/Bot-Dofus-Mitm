from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.CharacterBasicMinimalInformations import CharacterBasicMinimalInformations
class ArenaFighterLeaveMessage:
	def __init__(self, leaver:CharacterBasicMinimalInformations):
		self.leaver=leaver