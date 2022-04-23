from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AllianceModificationStartedMessage(NetworkMessage):
    canChangeName:bool
    canChangeTag:bool
    canChangeEmblem:bool
    canChangeName:bool
    canChangeTag:bool
    canChangeEmblem:bool
    

    def init(self, canChangeName_:bool, canChangeTag_:bool, canChangeEmblem_:bool):
        self.canChangeName = canChangeName_
        self.canChangeTag = canChangeTag_
        self.canChangeEmblem = canChangeEmblem_
        
        super().__init__()
    
    