from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorBasicInformations import TaxCollectorBasicInformations
    


class TaxCollectorMovementMessage(NetworkMessage):
    movementType:int
    basicInfos:'TaxCollectorBasicInformations'
    playerId:int
    playerName:str
    

    def init(self, movementType_:int, basicInfos_:'TaxCollectorBasicInformations', playerId_:int, playerName_:str):
        self.movementType = movementType_
        self.basicInfos = basicInfos_
        self.playerId = playerId_
        self.playerName = playerName_
        
        super().__init__()
    
    