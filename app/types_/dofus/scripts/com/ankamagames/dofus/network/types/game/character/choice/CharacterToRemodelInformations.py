from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.choice.CharacterRemodelingInformation import CharacterRemodelingInformation
if TYPE_CHECKING:
	...
class CharacterToRemodelInformations(CharacterRemodelingInformation):
	def __init__(self, possibleChangeMask:int, mandatoryChangeMask:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.possibleChangeMask=possibleChangeMask
		self.mandatoryChangeMask=mandatoryChangeMask