from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
class BreachInvitationResponseMessage:
	def __init__(self, guest:CharacterMinimalInformations, accept:bool):
		self.guest=guest
		self.accept=accept