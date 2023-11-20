from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
class MonsterInGroupInformations(MonsterInGroupLightInformations):
	def __init__(self, look:EntityLook, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.look=look