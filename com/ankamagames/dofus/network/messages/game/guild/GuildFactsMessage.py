from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.social.GuildFactSheetInformations import GuildFactSheetInformations
    from com.ankamagames.dofus.network.types.game.character.CharacterMinimalGuildPublicInformations import CharacterMinimalGuildPublicInformations
    


class GuildFactsMessage(NetworkMessage):
    infos:'GuildFactSheetInformations'
    creationDate:int
    nbTaxCollectors:int
    members:list['CharacterMinimalGuildPublicInformations']
    

    def init(self, infos_:'GuildFactSheetInformations', creationDate_:int, nbTaxCollectors_:int, members_:list['CharacterMinimalGuildPublicInformations']):
        self.infos = infos_
        self.creationDate = creationDate_
        self.nbTaxCollectors = nbTaxCollectors_
        self.members = members_
        
        super().__init__()
    
    