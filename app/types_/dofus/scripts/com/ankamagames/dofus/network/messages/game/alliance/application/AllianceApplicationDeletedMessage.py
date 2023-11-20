from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AllianceApplicationDeletedMessage:
	def __init__(self, deleted:bool):
		self.deleted=deleted