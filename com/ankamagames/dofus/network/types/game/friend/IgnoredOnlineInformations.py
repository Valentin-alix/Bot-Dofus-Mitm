from com.ankamagames.dofus.network.types.game.friend.IgnoredInformations import IgnoredInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class IgnoredOnlineInformations(IgnoredInformations):
    playerId:int
    playerName:str
    breed:int
    sex:bool
    

    def init(self, playerId_:int, playerName_:str, breed_:int, sex_:bool, accountId_:int, accountTag_:'AccountTagInformation'):
        self.playerId = playerId_
        self.playerName = playerName_
        self.breed = breed_
        self.sex = sex_
        
        super().__init__(accountId_, accountTag_)
    
    