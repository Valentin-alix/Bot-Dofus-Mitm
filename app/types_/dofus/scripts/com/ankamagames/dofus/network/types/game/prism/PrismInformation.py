from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class PrismInformation:
	def __init__(self, state:int, placementDate:int, nuggetsCount:int, durability:int, nextEvolutionDate:float):
		self.state=state
		self.placementDate=placementDate
		self.nuggetsCount=nuggetsCount
		self.durability=durability
		self.nextEvolutionDate=nextEvolutionDate