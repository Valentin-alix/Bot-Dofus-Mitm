from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CharacterDeletionRequestMessage(NetworkMessage):
    characterId:int
    secretAnswerHash:str
    

    def init(self, characterId_:int, secretAnswerHash_:str):
        self.characterId = characterId_
        self.secretAnswerHash = secretAnswerHash_
        
        super().__init__()
    
    