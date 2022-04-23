from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildInformationsGeneralMessage(NetworkMessage):
    abandonnedPaddock:bool
    level:int
    expLevelFloor:int
    experience:int
    expNextLevelFloor:int
    creationDate:int
    nbTotalMembers:int
    nbConnectedMembers:int
    

    def init(self, abandonnedPaddock_:bool, level_:int, expLevelFloor_:int, experience_:int, expNextLevelFloor_:int, creationDate_:int, nbTotalMembers_:int, nbConnectedMembers_:int):
        self.abandonnedPaddock = abandonnedPaddock_
        self.level = level_
        self.expLevelFloor = expLevelFloor_
        self.experience = experience_
        self.expNextLevelFloor = expNextLevelFloor_
        self.creationDate = creationDate_
        self.nbTotalMembers = nbTotalMembers_
        self.nbConnectedMembers = nbConnectedMembers_
        
        super().__init__()
    
    