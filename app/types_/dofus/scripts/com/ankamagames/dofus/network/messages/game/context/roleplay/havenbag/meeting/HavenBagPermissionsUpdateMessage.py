from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class HavenBagPermissionsUpdateMessage:
	def __init__(self, permissions:int):
		self.permissions=permissions