from com.ankamagames.dofus.network.types.game.context.fight.SpawnInformation import SpawnInformation


class SpawnCompanionInformation(SpawnInformation):
    modelId:int
    level:int
    summonerId:int
    ownerId:int
    

    def init(self, modelId_:int, level_:int, summonerId_:int, ownerId_:int):
        self.modelId = modelId_
        self.level = level_
        self.summonerId = summonerId_
        self.ownerId = ownerId_
        
        super().__init__()
    
    