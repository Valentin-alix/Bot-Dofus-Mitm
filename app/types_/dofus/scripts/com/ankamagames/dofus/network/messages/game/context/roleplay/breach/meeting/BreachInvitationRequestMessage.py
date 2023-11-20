from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class BreachInvitationRequestMessage:
	def __init__(self, guests:list[int]):
		self.guests=guests