from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupInformations import MonsterInGroupInformations
class GroupMonsterStaticInformations:
	def __init__(self, mainCreatureLightInfos:MonsterInGroupLightInformations, underlings:list[MonsterInGroupInformations]):
		self.mainCreatureLightInfos=mainCreatureLightInfos
		self.underlings=underlings