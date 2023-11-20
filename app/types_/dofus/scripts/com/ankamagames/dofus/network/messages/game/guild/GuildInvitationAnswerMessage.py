from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GuildInvitationAnswerMessage:
	def __init__(self, accept:bool):
		self.accept=accept