from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyGuestInformations import PartyGuestInformations
class PartyNewGuestMessage(AbstractPartyEventMessage):
	def __init__(self, guest:PartyGuestInformations, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.guest=guest