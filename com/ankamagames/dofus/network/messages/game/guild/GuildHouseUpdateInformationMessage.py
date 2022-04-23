from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.house.HouseInformationsForGuild import HouseInformationsForGuild
    


class GuildHouseUpdateInformationMessage(NetworkMessage):
    housesInformations:'HouseInformationsForGuild'
    

    def init(self, housesInformations_:'HouseInformationsForGuild'):
        self.housesInformations = housesInformations_
        
        super().__init__()
    
    