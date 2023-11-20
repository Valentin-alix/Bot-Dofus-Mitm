from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class HavenBagDailyLoteryMessage:
	def __init__(self, returnType:int, gameActionId:str):
		self.returnType=returnType
		self.gameActionId=gameActionId