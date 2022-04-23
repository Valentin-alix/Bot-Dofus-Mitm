from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class UpdateMapPlayersAgressableStatusMessage(NetworkMessage):
    playerIds:list[int]
    enable:list[int]
    

    def init(self, playerIds_:list[int], enable_:list[int]):
        self.playerIds = playerIds_
        self.enable = enable_
        
        super().__init__()
    
    