from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CharacterNameSuggestionSuccessMessage(NetworkMessage):
    suggestion:str
    

    def init(self, suggestion_:str):
        self.suggestion = suggestion_
        
        super().__init__()
    
    