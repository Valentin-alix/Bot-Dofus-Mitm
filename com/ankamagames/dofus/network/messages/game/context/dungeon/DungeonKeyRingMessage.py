from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DungeonKeyRingMessage(NetworkMessage):
    availables:list[int]
    unavailables:list[int]
    

    def init(self, availables_:list[int], unavailables_:list[int]):
        self.availables = availables_
        self.unavailables = unavailables_
        
        super().__init__()
    
    