from com.ankamagames.dofus.network.types.game.context.fight.SpawnInformation import SpawnInformation


class SpawnCharacterInformation(SpawnInformation):
    name:str
    level:int
    

    def init(self, name_:str, level_:int):
        self.name = name_
        self.level = level_
        
        super().__init__()
    
    