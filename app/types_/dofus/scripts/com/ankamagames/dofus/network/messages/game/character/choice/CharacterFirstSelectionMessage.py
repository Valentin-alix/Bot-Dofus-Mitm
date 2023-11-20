from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.character.choice.CharacterSelectionMessage import CharacterSelectionMessage
if TYPE_CHECKING:
	...
class CharacterFirstSelectionMessage(CharacterSelectionMessage):
	def __init__(self, doTutorial:bool, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.doTutorial=doTutorial