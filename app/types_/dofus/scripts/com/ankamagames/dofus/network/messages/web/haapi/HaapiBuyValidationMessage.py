from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.web.haapi.HaapiValidationMessage import HaapiValidationMessage
if TYPE_CHECKING:
	...
class HaapiBuyValidationMessage(HaapiValidationMessage):
	def __init__(self, amount:int, email:str, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.amount=amount
		self.email=email