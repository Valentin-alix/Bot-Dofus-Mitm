from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.BaseSpawnMonsterInformation import BaseSpawnMonsterInformation
if TYPE_CHECKING:
	...
class SpawnScaledMonsterInformation(BaseSpawnMonsterInformation):
	def __init__(self, creatureLevel:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.creatureLevel=creatureLevel