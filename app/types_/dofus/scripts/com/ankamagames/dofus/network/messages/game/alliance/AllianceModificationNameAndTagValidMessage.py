from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AllianceModificationNameAndTagValidMessage:
	def __init__(self, allianceName:str, allianceTag:str):
		self.allianceName=allianceName
		self.allianceTag=allianceTag