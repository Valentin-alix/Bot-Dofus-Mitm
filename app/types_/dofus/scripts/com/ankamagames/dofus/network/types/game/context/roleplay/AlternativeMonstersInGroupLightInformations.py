from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
class AlternativeMonstersInGroupLightInformations:
	def __init__(self, playerCount:int, monsters:list[MonsterInGroupLightInformations]):
		self.playerCount=playerCount
		self.monsters=monsters