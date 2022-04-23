from com.ankamagames.dofus.network.types.game.context.fight.BaseSpawnMonsterInformation import BaseSpawnMonsterInformation


class SpawnScaledMonsterInformation(BaseSpawnMonsterInformation):
    creatureLevel:int
    

    def init(self, creatureLevel_:int, creatureGenericId_:int):
        self.creatureLevel = creatureLevel_
        
        super().__init__(creatureGenericId_)
    
    