from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.GroupMonsterStaticInformations import GroupMonsterStaticInformations
class GameRolePlayGroupMonsterInformations(GameRolePlayActorInformations):
	def __init__(self, staticInfos:GroupMonsterStaticInformations, lootShare:int, alignmentSide:int, hasHardcoreDrop:bool, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.staticInfos=staticInfos
		self.lootShare=lootShare
		self.alignmentSide=alignmentSide
		self.hasHardcoreDrop=hasHardcoreDrop