from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.GroupMonsterStaticInformations import GroupMonsterStaticInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.AlternativeMonstersInGroupLightInformations import AlternativeMonstersInGroupLightInformations
class GroupMonsterStaticInformationsWithAlternatives(GroupMonsterStaticInformations):
	def __init__(self, alternatives:list[AlternativeMonstersInGroupLightInformations], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.alternatives=alternatives