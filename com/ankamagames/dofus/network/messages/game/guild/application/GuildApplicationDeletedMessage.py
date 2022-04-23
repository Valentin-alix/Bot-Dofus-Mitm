from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildApplicationDeletedMessage(NetworkMessage):
    deleted:bool
    

    def init(self, deleted_:bool):
        self.deleted = deleted_
        
        super().__init__()
    
    