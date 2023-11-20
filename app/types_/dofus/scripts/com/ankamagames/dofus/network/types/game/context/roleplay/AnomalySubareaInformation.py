from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AnomalySubareaInformation:
	def __init__(self, subAreaId:int, rewardRate:int, hasAnomaly:bool, anomalyClosingTime:int):
		self.subAreaId=subAreaId
		self.rewardRate=rewardRate
		self.hasAnomaly=hasAnomaly
		self.anomalyClosingTime=anomalyClosingTime