from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ConsoleCommandsListMessage:
	def __init__(self, aliases:list[str], args:list[str], descriptions:list[str]):
		self.aliases=aliases
		self.args=args
		self.descriptions=descriptions