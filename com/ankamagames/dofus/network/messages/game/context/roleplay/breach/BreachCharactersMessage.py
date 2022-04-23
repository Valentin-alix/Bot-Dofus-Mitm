from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BreachCharactersMessage(NetworkMessage):
    characters:list[int]
    

    def init(self, characters_:list[int]):
        self.characters = characters_
        
        super().__init__()
    
    