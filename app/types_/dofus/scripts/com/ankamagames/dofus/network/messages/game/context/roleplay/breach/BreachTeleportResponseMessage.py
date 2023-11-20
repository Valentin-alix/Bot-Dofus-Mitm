from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class BreachTeleportResponseMessage:
	def __init__(self, teleported:bool):
		self.teleported=teleported