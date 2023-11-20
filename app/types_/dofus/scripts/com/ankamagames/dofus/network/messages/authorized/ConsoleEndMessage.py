from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ConsoleEndMessage:
	def __init__(self, consoleUuid:int, isSuccess:bool):
		self.consoleUuid=consoleUuid
		self.isSuccess=isSuccess