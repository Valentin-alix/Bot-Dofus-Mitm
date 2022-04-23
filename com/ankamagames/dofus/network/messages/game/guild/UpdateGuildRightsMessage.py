from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class UpdateGuildRightsMessage(NetworkMessage):
    rankId:int
    rights:list[int]
    

    def init(self, rankId_:int, rights_:list[int]):
        self.rankId = rankId_
        self.rights = rights_
        
        super().__init__()
    
    