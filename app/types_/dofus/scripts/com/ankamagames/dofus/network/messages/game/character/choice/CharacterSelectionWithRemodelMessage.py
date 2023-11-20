from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.character.choice.CharacterSelectionMessage import CharacterSelectionMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.choice.RemodelingInformation import RemodelingInformation
class CharacterSelectionWithRemodelMessage(CharacterSelectionMessage):
	def __init__(self, remodel:RemodelingInformation, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.remodel=remodel