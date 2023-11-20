from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class Contribution:
	def __init__(self, contributorId:int, contributorName:str, amount:int):
		self.contributorId=contributorId
		self.contributorName=contributorName
		self.amount=amount