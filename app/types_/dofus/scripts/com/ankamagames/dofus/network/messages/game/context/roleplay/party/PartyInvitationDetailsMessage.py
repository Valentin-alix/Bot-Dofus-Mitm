from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyInvitationMemberInformations import PartyInvitationMemberInformations
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyGuestInformations import PartyGuestInformations
class PartyInvitationDetailsMessage(AbstractPartyMessage):
	def __init__(self, partyType:int, partyName:str, fromId:int, fromName:str, leaderId:int, members:list[PartyInvitationMemberInformations], guests:list[PartyGuestInformations], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.partyType=partyType
		self.partyName=partyName
		self.fromId=fromId
		self.fromName=fromName
		self.leaderId=leaderId
		self.members=members
		self.guests=guests