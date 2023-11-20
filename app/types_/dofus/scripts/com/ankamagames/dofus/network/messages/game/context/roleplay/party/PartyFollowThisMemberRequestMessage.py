from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyFollowMemberRequestMessage import PartyFollowMemberRequestMessage
if TYPE_CHECKING:
	...
class PartyFollowThisMemberRequestMessage(PartyFollowMemberRequestMessage):
	def __init__(self, enabled:bool, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.enabled=enabled