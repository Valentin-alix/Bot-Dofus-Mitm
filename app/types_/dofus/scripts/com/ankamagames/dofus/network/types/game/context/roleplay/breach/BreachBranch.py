from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
class BreachBranch:
	def __init__(self, room:int, element:int, bosses:list[MonsterInGroupLightInformations], map:float, score:int, relativeScore:int, monsters:list[MonsterInGroupLightInformations]):
		self.room=room
		self.element=element
		self.bosses=bosses
		self.map=map
		self.score=score
		self.relativeScore=relativeScore
		self.monsters=monsters