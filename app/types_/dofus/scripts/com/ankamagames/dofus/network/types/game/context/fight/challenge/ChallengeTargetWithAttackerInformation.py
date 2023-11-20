from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.challenge.ChallengeTargetInformation import ChallengeTargetInformation
if TYPE_CHECKING:
	...
class ChallengeTargetWithAttackerInformation(ChallengeTargetInformation):
	def __init__(self, attackersIds:list[float], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.attackersIds=attackersIds