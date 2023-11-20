from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.character.stats.CharacterLevelUpMessage import CharacterLevelUpMessage
if TYPE_CHECKING:
	...
class CharacterLevelUpInformationMessage(CharacterLevelUpMessage):
	def __init__(self, name:str, id:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.name=name
		self.id=id