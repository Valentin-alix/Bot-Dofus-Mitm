from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayGroupMonsterInformations import GameRolePlayGroupMonsterInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.GroupMonsterStaticInformations import GroupMonsterStaticInformations
class GameRolePlayGroupMonsterWaveInformations(GameRolePlayGroupMonsterInformations):
	def __init__(self, nbWaves:int, alternatives:list[GroupMonsterStaticInformations], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.nbWaves=nbWaves
		self.alternatives=alternatives