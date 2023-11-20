from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMemberInFightMessage import AbstractPartyMemberInFightMessage
if TYPE_CHECKING:
	...
class PartyMemberInBreachFightMessage(AbstractPartyMemberInFightMessage):
	def __init__(self, floor:int, room:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.floor=floor
		self.room=room