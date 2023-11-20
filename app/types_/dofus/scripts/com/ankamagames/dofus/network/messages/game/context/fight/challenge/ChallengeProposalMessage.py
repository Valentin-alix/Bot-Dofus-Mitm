from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.challenge.ChallengeInformation import ChallengeInformation
class ChallengeProposalMessage:
	def __init__(self, challengeProposals:list[ChallengeInformation], timer:float):
		self.challengeProposals=challengeProposals
		self.timer=timer