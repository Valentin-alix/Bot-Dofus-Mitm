from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildApplicationListenMessage(NetworkMessage):
    listen:bool
    

    def init(self, listen_:bool):
        self.listen = listen_
        
        super().__init__()
    
    