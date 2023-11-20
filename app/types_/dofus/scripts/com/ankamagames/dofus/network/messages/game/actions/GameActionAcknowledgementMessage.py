from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameActionAcknowledgementMessage:
	def __init__(self, valid:bool, actionId:int):
		self.valid=valid
		self.actionId=actionId