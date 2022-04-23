from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class KnownZaapListMessage(NetworkMessage):
    destinations:list[int]
    

    def init(self, destinations_:list[int]):
        self.destinations = destinations_
        
        super().__init__()
    
    