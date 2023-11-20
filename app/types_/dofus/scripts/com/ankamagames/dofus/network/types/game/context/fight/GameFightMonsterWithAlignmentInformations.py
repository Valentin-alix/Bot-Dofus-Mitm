from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.GameFightMonsterInformations import GameFightMonsterInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.alignment.ActorAlignmentInformations import ActorAlignmentInformations
class GameFightMonsterWithAlignmentInformations(GameFightMonsterInformations):
	def __init__(self, alignmentInfos:ActorAlignmentInformations, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.alignmentInfos=alignmentInfos