from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ContactLookRequestMessage:
	def __init__(self, requestId:int, contactType:int):
		self.requestId=requestId
		self.contactType=contactType