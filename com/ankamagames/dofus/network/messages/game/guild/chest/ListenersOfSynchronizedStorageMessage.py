from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ListenersOfSynchronizedStorageMessage(NetworkMessage):
    players:list[str]
    

    def init(self, players_:list[str]):
        self.players = players_
        
        super().__init__()
    
    