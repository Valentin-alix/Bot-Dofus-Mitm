from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.SpawnInformation import SpawnInformation
if TYPE_CHECKING:
	...
class SpawnCompanionInformation(SpawnInformation):
	def __init__(self, modelId:int, level:int, summonerId:float, ownerId:float, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.modelId=modelId
		self.level=level
		self.summonerId=summonerId
		self.ownerId=ownerId