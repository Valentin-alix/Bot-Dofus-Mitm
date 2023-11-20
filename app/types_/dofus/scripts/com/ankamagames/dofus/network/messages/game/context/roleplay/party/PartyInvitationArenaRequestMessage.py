from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyInvitationRequestMessage import PartyInvitationRequestMessage
if TYPE_CHECKING:
	...
class PartyInvitationArenaRequestMessage(PartyInvitationRequestMessage):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		...