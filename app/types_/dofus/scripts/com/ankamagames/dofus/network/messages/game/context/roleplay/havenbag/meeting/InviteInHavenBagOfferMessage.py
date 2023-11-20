from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
class InviteInHavenBagOfferMessage:
	def __init__(self, hostInformations:CharacterMinimalInformations, timeLeftBeforeCancel:int):
		self.hostInformations=hostInformations
		self.timeLeftBeforeCancel=timeLeftBeforeCancel