from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ReloginTokenStatusMessage:
	def __init__(self, validToken:bool, token:str):
		self.validToken=validToken
		self.token=token