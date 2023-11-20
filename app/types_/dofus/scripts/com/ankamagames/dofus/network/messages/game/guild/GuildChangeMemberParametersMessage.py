from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GuildChangeMemberParametersMessage:
	def __init__(self, memberId:int, rankId:int, experienceGivenPercent:int):
		self.memberId=memberId
		self.rankId=rankId
		self.experienceGivenPercent=experienceGivenPercent