from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyMemberInformations import PartyMemberInformations
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyGuestInformations import PartyGuestInformations
class PartyJoinMessage(AbstractPartyMessage):
	def __init__(self, partyType:int, partyLeaderId:int, maxParticipants:int, members:list[PartyMemberInformations], guests:list[PartyGuestInformations], restricted:bool, partyName:str, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.partyType=partyType
		self.partyLeaderId=partyLeaderId
		self.maxParticipants=maxParticipants
		self.members=members
		self.guests=guests
		self.restricted=restricted
		self.partyName=partyName