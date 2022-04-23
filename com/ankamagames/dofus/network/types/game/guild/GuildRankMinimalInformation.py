from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildRankMinimalInformation(NetworkMessage):
    id:int
    name:str
    

    def init(self, id_:int, name_:str):
        self.id = id_
        self.name = name_
        
        super().__init__()
    
    