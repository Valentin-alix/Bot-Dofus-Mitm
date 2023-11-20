from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.character.choice.CharactersListMessage import CharactersListMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.choice.CharacterToRemodelInformations import CharacterToRemodelInformations
class CharactersListWithRemodelingMessage(CharactersListMessage):
	def __init__(self, charactersToRemodel:list[CharacterToRemodelInformations], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.charactersToRemodel=charactersToRemodel