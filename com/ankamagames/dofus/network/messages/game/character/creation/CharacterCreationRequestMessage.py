from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CharacterCreationRequestMessage(NetworkMessage):
    name:str
    breed:int
    sex:bool
    colors:list[int]
    cosmeticId:int
    

    def init(self, name_:str, breed_:int, sex_:bool, colors_:list[int], cosmeticId_:int):
        self.name = name_
        self.breed = breed_
        self.sex = sex_
        self.colors = colors_
        self.cosmeticId = cosmeticId_
        
        super().__init__()
    
    