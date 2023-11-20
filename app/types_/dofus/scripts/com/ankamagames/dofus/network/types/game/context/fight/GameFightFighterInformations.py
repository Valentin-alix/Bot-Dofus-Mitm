from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.GameContextActorInformations import GameContextActorInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacteristics import GameFightCharacteristics
class GameFightFighterInformations(GameContextActorInformations):
	def __init__(self, spawnInfo:GameContextBasicSpawnInformation, wave:int, stats:GameFightCharacteristics, previousPositions:list[int], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.spawnInfo=spawnInfo
		self.wave=wave
		self.stats=stats
		self.previousPositions=previousPositions