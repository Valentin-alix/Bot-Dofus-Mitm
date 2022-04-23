from com.ankamagames.dofus.network.messages.game.character.stats.CharacterLevelUpMessage import CharacterLevelUpMessage


class CharacterLevelUpInformationMessage(CharacterLevelUpMessage):
    name:str
    id:int
    

    def init(self, name_:str, id_:int, newLevel_:int):
        self.name = name_
        self.id = id_
        
        super().__init__(newLevel_)
    
    