from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.house.HouseInformations import HouseInformations
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.interactive.InteractiveElement import InteractiveElement
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.interactive.StatedElement import StatedElement
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.interactive.MapObstacle import MapObstacle
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightCommonInformations import FightCommonInformations
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightStartingPositions import FightStartingPositions
class MapComplementaryInformationsDataMessage:
	def __init__(self, subAreaId:int, mapId:float, houses:list[HouseInformations], actors:list[GameRolePlayActorInformations], interactiveElements:list[InteractiveElement], statedElements:list[StatedElement], obstacles:list[MapObstacle], fights:list[FightCommonInformations], hasAggressiveMonsters:bool, fightStartPositions:FightStartingPositions):
		self.subAreaId=subAreaId
		self.mapId=mapId
		self.houses=houses
		self.actors=actors
		self.interactiveElements=interactiveElements
		self.statedElements=statedElements
		self.obstacles=obstacles
		self.fights=fights
		self.hasAggressiveMonsters=hasAggressiveMonsters
		self.fightStartPositions=fightStartPositions