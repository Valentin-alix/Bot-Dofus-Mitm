from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class TeleportPlayerAnswerMessage:
	def __init__(self, accept:bool, requesterId:int):
		self.accept=accept
		self.requesterId=requesterId