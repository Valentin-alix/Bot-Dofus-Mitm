from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismsListRegisterMessage(NetworkMessage):
    listen:int
    

    def init(self, listen_:int):
        self.listen = listen_
        
        super().__init__()
    
    