from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameRolePlayArenaSwitchToGameServerMessage:
	def __init__(self, validToken:bool, token:str, homeServerId:int):
		self.validToken=validToken
		self.token=token
		self.homeServerId=homeServerId