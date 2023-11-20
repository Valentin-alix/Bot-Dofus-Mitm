from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.challenge.ChallengeInformation import ChallengeInformation
class ChallengeListMessage:
	def __init__(self, challengesInformation:list[ChallengeInformation]):
		self.challengesInformation=challengesInformation