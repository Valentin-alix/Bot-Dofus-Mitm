from com.ankamagames.dofus.network.messages.game.inventory.items.ObjectUseMessage import ObjectUseMessage


class ObjectUseOnCharacterMessage(ObjectUseMessage):
    characterId:int
    

    def init(self, characterId_:int, objectUID_:int):
        self.characterId = characterId_
        
        super().__init__(objectUID_)
    
    