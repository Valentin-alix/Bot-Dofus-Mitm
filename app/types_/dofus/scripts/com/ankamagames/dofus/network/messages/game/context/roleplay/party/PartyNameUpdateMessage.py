from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage
if TYPE_CHECKING:
	...
class PartyNameUpdateMessage(AbstractPartyMessage):
	def __init__(self, partyName:str, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.partyName=partyName