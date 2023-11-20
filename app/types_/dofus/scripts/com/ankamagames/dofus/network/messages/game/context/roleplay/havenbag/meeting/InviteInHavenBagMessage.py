from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
class InviteInHavenBagMessage:
	def __init__(self, guestInformations:CharacterMinimalInformations, accept:bool):
		self.guestInformations=guestInformations
		self.accept=accept