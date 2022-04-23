from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyMemberInformations import PartyMemberInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyGuestInformations import PartyGuestInformations
    


class PartyJoinMessage(AbstractPartyMessage):
    partyType:int
    partyLeaderId:int
    maxParticipants:int
    members:list['PartyMemberInformations']
    guests:list['PartyGuestInformations']
    restricted:bool
    partyName:str
    

    def init(self, partyType_:int, partyLeaderId_:int, maxParticipants_:int, members_:list['PartyMemberInformations'], guests_:list['PartyGuestInformations'], restricted_:bool, partyName_:str, partyId_:int):
        self.partyType = partyType_
        self.partyLeaderId = partyLeaderId_
        self.maxParticipants = maxParticipants_
        self.members = members_
        self.guests = guests_
        self.restricted = restricted_
        self.partyName = partyName_
        
        super().__init__(partyId_)
    
    