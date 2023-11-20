from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.BasicNamedAllianceInformations import BasicNamedAllianceInformations
class CharacterMinimalAllianceInformations(CharacterMinimalPlusLookInformations):
	def __init__(self, alliance:BasicNamedAllianceInformations, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.alliance=alliance