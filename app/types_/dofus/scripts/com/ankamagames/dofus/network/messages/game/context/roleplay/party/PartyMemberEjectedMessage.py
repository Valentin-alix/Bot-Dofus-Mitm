from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyMemberRemoveMessage import PartyMemberRemoveMessage
if TYPE_CHECKING:
	...
class PartyMemberEjectedMessage(PartyMemberRemoveMessage):
	def __init__(self, kickerId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.kickerId=kickerId