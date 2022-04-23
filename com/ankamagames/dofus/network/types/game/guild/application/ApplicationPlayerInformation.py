from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
    


class ApplicationPlayerInformation(NetworkMessage):
    playerId:int
    playerName:str
    breed:int
    sex:bool
    level:int
    accountId:int
    accountTag:str
    accountNickname:str
    status:'PlayerStatus'
    

    def init(self, playerId_:int, playerName_:str, breed_:int, sex_:bool, level_:int, accountId_:int, accountTag_:str, accountNickname_:str, status_:'PlayerStatus'):
        self.playerId = playerId_
        self.playerName = playerName_
        self.breed = breed_
        self.sex = sex_
        self.level = level_
        self.accountId = accountId_
        self.accountTag = accountTag_
        self.accountNickname = accountNickname_
        self.status = status_
        
        super().__init__()
    
    