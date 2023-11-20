from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage
if TYPE_CHECKING:
	...
class PartyInvitationMessage(AbstractPartyMessage):
	def __init__(self, partyType:int, partyName:str, maxParticipants:int, fromId:int, fromName:str, toId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.partyType=partyType
		self.partyName=partyName
		self.maxParticipants=maxParticipants
		self.fromId=fromId
		self.fromName=fromName
		self.toId=toId