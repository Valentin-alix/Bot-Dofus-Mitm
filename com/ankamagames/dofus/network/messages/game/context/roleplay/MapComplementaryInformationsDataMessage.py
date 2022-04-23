from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.house.HouseInformations import HouseInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
    from com.ankamagames.dofus.network.types.game.interactive.InteractiveElement import InteractiveElement
    from com.ankamagames.dofus.network.types.game.interactive.StatedElement import StatedElement
    from com.ankamagames.dofus.network.types.game.interactive.MapObstacle import MapObstacle
    from com.ankamagames.dofus.network.types.game.context.fight.FightCommonInformations import FightCommonInformations
    from com.ankamagames.dofus.network.types.game.context.fight.FightStartingPositions import FightStartingPositions
    


class MapComplementaryInformationsDataMessage(NetworkMessage):
    subAreaId:int
    mapId:int
    houses:list['HouseInformations']
    actors:list['GameRolePlayActorInformations']
    interactiveElements:list['InteractiveElement']
    statedElements:list['StatedElement']
    obstacles:list['MapObstacle']
    fights:list['FightCommonInformations']
    hasAggressiveMonsters:bool
    fightStartPositions:'FightStartingPositions'
    

    def init(self, subAreaId_:int, mapId_:int, houses_:list['HouseInformations'], actors_:list['GameRolePlayActorInformations'], interactiveElements_:list['InteractiveElement'], statedElements_:list['StatedElement'], obstacles_:list['MapObstacle'], fights_:list['FightCommonInformations'], hasAggressiveMonsters_:bool, fightStartPositions_:'FightStartingPositions'):
        self.subAreaId = subAreaId_
        self.mapId = mapId_
        self.houses = houses_
        self.actors = actors_
        self.interactiveElements = interactiveElements_
        self.statedElements = statedElements_
        self.obstacles = obstacles_
        self.fights = fights_
        self.hasAggressiveMonsters = hasAggressiveMonsters_
        self.fightStartPositions = fightStartPositions_
        
        super().__init__()
    
    