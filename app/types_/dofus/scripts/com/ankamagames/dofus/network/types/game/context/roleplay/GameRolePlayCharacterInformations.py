from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayHumanoidInformations import GameRolePlayHumanoidInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.alignment.ActorAlignmentInformations import ActorAlignmentInformations
class GameRolePlayCharacterInformations(GameRolePlayHumanoidInformations):
	def __init__(self, alignmentInfos:ActorAlignmentInformations, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.alignmentInfos=alignmentInfos