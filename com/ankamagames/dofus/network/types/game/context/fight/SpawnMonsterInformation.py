from com.ankamagames.dofus.network.types.game.context.fight.BaseSpawnMonsterInformation import BaseSpawnMonsterInformation


class SpawnMonsterInformation(BaseSpawnMonsterInformation):
    creatureGrade:int
    

    def init(self, creatureGrade_:int, creatureGenericId_:int):
        self.creatureGrade = creatureGrade_
        
        super().__init__(creatureGenericId_)
    
    