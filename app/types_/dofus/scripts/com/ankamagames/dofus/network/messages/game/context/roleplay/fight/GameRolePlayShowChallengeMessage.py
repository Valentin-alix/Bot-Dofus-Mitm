from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightCommonInformations import FightCommonInformations
class GameRolePlayShowChallengeMessage:
	def __init__(self, commonsInfos:FightCommonInformations):
		self.commonsInfos=commonsInfos