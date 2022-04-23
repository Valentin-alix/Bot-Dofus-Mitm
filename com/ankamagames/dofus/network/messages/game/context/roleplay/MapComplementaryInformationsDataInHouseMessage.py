from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.house.HouseInformationsInside import HouseInformationsInside
    from com.ankamagames.dofus.network.types.game.house.HouseInformations import HouseInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
    from com.ankamagames.dofus.network.types.game.interactive.InteractiveElement import InteractiveElement
    from com.ankamagames.dofus.network.types.game.interactive.StatedElement import StatedElement
    from com.ankamagames.dofus.network.types.game.interactive.MapObstacle import MapObstacle
    from com.ankamagames.dofus.network.types.game.context.fight.FightCommonInformations import FightCommonInformations
    from com.ankamagames.dofus.network.types.game.context.fight.FightStartingPositions import FightStartingPositions
    


class MapComplementaryInformationsDataInHouseMessage(MapComplementaryInformationsDataMessage):
    currentHouse:'HouseInformationsInside'
    

    def init(self, currentHouse_:'HouseInformationsInside', subAreaId_:int, mapId_:int, houses_:list['HouseInformations'], actors_:list['GameRolePlayActorInformations'], interactiveElements_:list['InteractiveElement'], statedElements_:list['StatedElement'], obstacles_:list['MapObstacle'], fights_:list['FightCommonInformations'], hasAggressiveMonsters_:bool, fightStartPositions_:'FightStartingPositions'):
        self.currentHouse = currentHouse_
        
        super().__init__(subAreaId_, mapId_, houses_, actors_, interactiveElements_, statedElements_, obstacles_, fights_, hasAggressiveMonsters_, fightStartPositions_)
    
    