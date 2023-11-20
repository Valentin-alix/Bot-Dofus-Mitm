from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GuildInvitationStateRecruterMessage:
	def __init__(self, recrutedName:str, invitationState:int):
		self.recrutedName=recrutedName
		self.invitationState=invitationState