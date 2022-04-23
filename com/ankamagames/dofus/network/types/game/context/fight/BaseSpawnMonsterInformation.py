from com.ankamagames.dofus.network.types.game.context.fight.SpawnInformation import SpawnInformation


class BaseSpawnMonsterInformation(SpawnInformation):
    creatureGenericId:int
    

    def init(self, creatureGenericId_:int):
        self.creatureGenericId = creatureGenericId_
        
        super().__init__()
    
    