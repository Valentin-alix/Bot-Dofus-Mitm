from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GuildChestTabContributionMessage:
	def __init__(self, tabNumber:int, requiredAmount:int, currentAmount:int, chestContributionEnrollmentDelay:float, chestContributionDelay:float):
		self.tabNumber=tabNumber
		self.requiredAmount=requiredAmount
		self.currentAmount=currentAmount
		self.chestContributionEnrollmentDelay=chestContributionEnrollmentDelay
		self.chestContributionDelay=chestContributionDelay