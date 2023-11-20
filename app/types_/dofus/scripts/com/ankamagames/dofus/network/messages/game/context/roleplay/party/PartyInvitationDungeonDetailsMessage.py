from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyInvitationDetailsMessage import PartyInvitationDetailsMessage
if TYPE_CHECKING:
	...
class PartyInvitationDungeonDetailsMessage(PartyInvitationDetailsMessage):
	def __init__(self, dungeonId:int, playersDungeonReady:list[bool], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.dungeonId=dungeonId
		self.playersDungeonReady=playersDungeonReady