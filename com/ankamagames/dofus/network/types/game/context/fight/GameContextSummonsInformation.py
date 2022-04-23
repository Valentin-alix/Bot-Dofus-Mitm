from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.SpawnInformation import SpawnInformation
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacteristics import GameFightCharacteristics
    from com.ankamagames.dofus.network.types.game.context.fight.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
    


class GameContextSummonsInformation(NetworkMessage):
    spawnInformation:'SpawnInformation'
    wave:int
    look:'EntityLook'
    stats:'GameFightCharacteristics'
    summons:list['GameContextBasicSpawnInformation']
    

    def init(self, spawnInformation_:'SpawnInformation', wave_:int, look_:'EntityLook', stats_:'GameFightCharacteristics', summons_:list['GameContextBasicSpawnInformation']):
        self.spawnInformation = spawnInformation_
        self.wave = wave_
        self.look = look_
        self.stats = stats_
        self.summons = summons_
        
        super().__init__()
    
    