from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildModificationStartedMessage(NetworkMessage):
    canChangeName:bool
    canChangeEmblem:bool
    canChangeName:bool
    canChangeEmblem:bool
    

    def init(self, canChangeName_:bool, canChangeEmblem_:bool):
        self.canChangeName = canChangeName_
        self.canChangeEmblem = canChangeEmblem_
        
        super().__init__()
    
    