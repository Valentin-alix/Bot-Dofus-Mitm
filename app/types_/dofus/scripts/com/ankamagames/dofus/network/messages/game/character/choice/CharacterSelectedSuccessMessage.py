from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations
class CharacterSelectedSuccessMessage:
	def __init__(self, infos:CharacterBaseInformations, isCollectingStats:bool):
		self.infos=infos
		self.isCollectingStats=isCollectingStats