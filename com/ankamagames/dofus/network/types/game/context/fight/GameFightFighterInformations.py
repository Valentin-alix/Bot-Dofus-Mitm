from com.ankamagames.dofus.network.types.game.context.GameContextActorInformations import GameContextActorInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacteristics import GameFightCharacteristics
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameFightFighterInformations(GameContextActorInformations):
    spawnInfo:'GameContextBasicSpawnInformation'
    wave:int
    stats:'GameFightCharacteristics'
    previousPositions:list[int]
    

    def init(self, spawnInfo_:'GameContextBasicSpawnInformation', wave_:int, stats_:'GameFightCharacteristics', previousPositions_:list[int], look_:'EntityLook', contextualId_:int, disposition_:'EntityDispositionInformations'):
        self.spawnInfo = spawnInfo_
        self.wave = wave_
        self.stats = stats_
        self.previousPositions = previousPositions_
        
        super().__init__(look_, contextualId_, disposition_)
    
    