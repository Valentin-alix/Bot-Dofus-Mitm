from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMemberInFightMessage import AbstractPartyMemberInFightMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.MapCoordinatesExtended import MapCoordinatesExtended
    


class PartyMemberInStandardFightMessage(AbstractPartyMemberInFightMessage):
    fightMap:'MapCoordinatesExtended'
    

    def init(self, fightMap_:'MapCoordinatesExtended', reason_:int, memberId_:int, memberAccountId_:int, memberName_:str, fightId_:int, timeBeforeFightStart_:int, partyId_:int):
        self.fightMap = fightMap_
        
        super().__init__(reason_, memberId_, memberAccountId_, memberName_, fightId_, timeBeforeFightStart_, partyId_)
    
    