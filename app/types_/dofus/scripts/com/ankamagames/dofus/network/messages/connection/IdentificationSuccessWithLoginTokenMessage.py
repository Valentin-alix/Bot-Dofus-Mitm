from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.connection.IdentificationSuccessMessage import IdentificationSuccessMessage
if TYPE_CHECKING:
	...
class IdentificationSuccessWithLoginTokenMessage(IdentificationSuccessMessage):
	def __init__(self, loginToken:str, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.loginToken=loginToken