from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage
if TYPE_CHECKING:
	...
class AbstractPartyMemberInFightMessage(AbstractPartyMessage):
	def __init__(self, reason:int, memberId:int, memberAccountId:int, memberName:str, fightId:int, timeBeforeFightStart:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.reason=reason
		self.memberId=memberId
		self.memberAccountId=memberAccountId
		self.memberName=memberName
		self.fightId=fightId
		self.timeBeforeFightStart=timeBeforeFightStart