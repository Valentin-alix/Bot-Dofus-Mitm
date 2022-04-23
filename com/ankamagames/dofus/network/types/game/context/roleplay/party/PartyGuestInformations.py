from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.entity.PartyEntityBaseInformation import PartyEntityBaseInformation
    


class PartyGuestInformations(NetworkMessage):
    guestId:int
    hostId:int
    name:str
    guestLook:'EntityLook'
    breed:int
    sex:bool
    status:'PlayerStatus'
    entities:list['PartyEntityBaseInformation']
    

    def init(self, guestId_:int, hostId_:int, name_:str, guestLook_:'EntityLook', breed_:int, sex_:bool, status_:'PlayerStatus', entities_:list['PartyEntityBaseInformation']):
        self.guestId = guestId_
        self.hostId = hostId_
        self.name = name_
        self.guestLook = guestLook_
        self.breed = breed_
        self.sex = sex_
        self.status = status_
        self.entities = entities_
        
        super().__init__()
    
    