from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class LockableStateUpdateAbstractMessage:
	def __init__(self, locked:bool):
		self.locked=locked