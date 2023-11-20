from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class MigratedServerListMessage:
	def __init__(self, migratedServerIds:list[int]):
		self.migratedServerIds=migratedServerIds