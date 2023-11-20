from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AllianceSubmitApplicationMessage:
	def __init__(self, applyText:str, allianceId:int):
		self.applyText=applyText
		self.allianceId=allianceId