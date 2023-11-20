from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.MonsterBoosts import MonsterBoosts
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.MonsterBoosts import MonsterBoosts
class GameRefreshMonsterBoostsMessage:
	def __init__(self, monsterBoosts:list[MonsterBoosts], familyBoosts:list[MonsterBoosts]):
		self.monsterBoosts=monsterBoosts
		self.familyBoosts=familyBoosts