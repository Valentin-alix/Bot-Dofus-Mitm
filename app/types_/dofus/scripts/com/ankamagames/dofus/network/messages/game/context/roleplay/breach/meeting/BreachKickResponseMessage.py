from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
class BreachKickResponseMessage:
	def __init__(self, target:CharacterMinimalInformations, kicked:bool):
		self.target=target
		self.kicked=kicked