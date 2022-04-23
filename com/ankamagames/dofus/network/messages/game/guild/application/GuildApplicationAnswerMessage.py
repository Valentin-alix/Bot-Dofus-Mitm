from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildApplicationAnswerMessage(NetworkMessage):
    accepted:bool
    playerId:int
    

    def init(self, accepted_:bool, playerId_:int):
        self.accepted = accepted_
        self.playerId = playerId_
        
        super().__init__()
    
    