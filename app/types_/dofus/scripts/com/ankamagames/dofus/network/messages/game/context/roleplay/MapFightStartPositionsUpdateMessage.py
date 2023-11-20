from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightStartingPositions import FightStartingPositions
class MapFightStartPositionsUpdateMessage:
	def __init__(self, mapId:float, fightStartPositions:FightStartingPositions):
		self.mapId=mapId
		self.fightStartPositions=fightStartPositions