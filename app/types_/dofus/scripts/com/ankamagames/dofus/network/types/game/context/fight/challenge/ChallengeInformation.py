from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.challenge.ChallengeTargetInformation import ChallengeTargetInformation
class ChallengeInformation:
	def __init__(self, challengeId:int, targetsList:list[ChallengeTargetInformation], dropBonus:int, xpBonus:int, state:int):
		self.challengeId=challengeId
		self.targetsList=targetsList
		self.dropBonus=dropBonus
		self.xpBonus=xpBonus
		self.state=state