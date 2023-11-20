from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AllianceInvitationStateRecruterMessage:
	def __init__(self, recrutedName:str, invitationState:int):
		self.recrutedName=recrutedName
		self.invitationState=invitationState