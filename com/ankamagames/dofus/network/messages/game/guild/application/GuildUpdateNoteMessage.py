from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildUpdateNoteMessage(NetworkMessage):
    memberId:int
    note:str
    

    def init(self, memberId_:int, note_:str):
        self.memberId = memberId_
        self.note = note_
        
        super().__init__()
    
    