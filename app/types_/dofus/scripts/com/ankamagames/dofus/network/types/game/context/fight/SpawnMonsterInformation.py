from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.BaseSpawnMonsterInformation import BaseSpawnMonsterInformation
if TYPE_CHECKING:
	...
class SpawnMonsterInformation(BaseSpawnMonsterInformation):
	def __init__(self, creatureGrade:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.creatureGrade=creatureGrade