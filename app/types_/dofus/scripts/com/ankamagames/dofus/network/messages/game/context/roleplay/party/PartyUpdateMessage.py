from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyMemberInformations import PartyMemberInformations
class PartyUpdateMessage(AbstractPartyEventMessage):
	def __init__(self, memberInformations:PartyMemberInformations, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.memberInformations=memberInformations