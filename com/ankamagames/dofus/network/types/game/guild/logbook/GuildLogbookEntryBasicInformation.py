from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildLogbookEntryBasicInformation(NetworkMessage):
    id:int
    date:int
    

    def init(self, id_:int, date_:int):
        self.id = id_
        self.date = date_
        
        super().__init__()
    
    