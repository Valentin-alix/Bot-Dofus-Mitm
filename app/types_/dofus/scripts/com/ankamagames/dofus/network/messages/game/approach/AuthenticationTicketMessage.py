from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AuthenticationTicketMessage:
	def __init__(self, lang:str, ticket:str):
		self.lang=lang
		self.ticket=ticket