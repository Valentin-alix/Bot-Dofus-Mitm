from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CharacterSelectionMessage(NetworkMessage):
    id:int
    

    def init(self, id_:int):
        self.id = id_
        
        super().__init__()
    
    