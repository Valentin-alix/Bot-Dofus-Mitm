from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameActionFightNoSpellCastMessage(NetworkMessage):
    spellLevelId:int
    

    def init(self, spellLevelId_:int):
        self.spellLevelId = spellLevelId_
        
        super().__init__()
    
    