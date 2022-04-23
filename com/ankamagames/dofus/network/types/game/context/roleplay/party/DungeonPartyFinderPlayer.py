from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DungeonPartyFinderPlayer(NetworkMessage):
    playerId:int
    playerName:str
    breed:int
    sex:bool
    level:int
    

    def init(self, playerId_:int, playerName_:str, breed_:int, sex_:bool, level_:int):
        self.playerId = playerId_
        self.playerName = playerName_
        self.breed = breed_
        self.sex = sex_
        self.level = level_
        
        super().__init__()
    
    