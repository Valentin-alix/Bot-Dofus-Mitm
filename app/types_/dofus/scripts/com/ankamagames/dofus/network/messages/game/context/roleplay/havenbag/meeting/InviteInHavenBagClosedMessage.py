from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
class InviteInHavenBagClosedMessage:
	def __init__(self, hostInformations:CharacterMinimalInformations):
		self.hostInformations=hostInformations