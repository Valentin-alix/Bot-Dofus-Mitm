from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ListenersOfSynchronizedStorageMessage:
	def __init__(self, players:list[str]):
		self.players=players