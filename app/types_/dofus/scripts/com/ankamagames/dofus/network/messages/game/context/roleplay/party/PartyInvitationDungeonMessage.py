from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyInvitationMessage import PartyInvitationMessage
if TYPE_CHECKING:
	...
class PartyInvitationDungeonMessage(PartyInvitationMessage):
	def __init__(self, dungeonId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.dungeonId=dungeonId