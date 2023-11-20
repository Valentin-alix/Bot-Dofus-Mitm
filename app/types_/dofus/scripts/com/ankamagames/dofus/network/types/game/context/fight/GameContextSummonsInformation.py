from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.SpawnInformation import SpawnInformation
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacteristics import GameFightCharacteristics
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
class GameContextSummonsInformation:
	def __init__(self, spawnInformation:SpawnInformation, wave:int, look:EntityLook, stats:GameFightCharacteristics, summons:list[GameContextBasicSpawnInformation]):
		self.spawnInformation=spawnInformation
		self.wave=wave
		self.look=look
		self.stats=stats
		self.summons=summons