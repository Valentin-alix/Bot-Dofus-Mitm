from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class HaapiConfirmationMessage:
	def __init__(self, kamas:int, amount:int, rate:int, action:int, transaction:str):
		self.kamas=kamas
		self.amount=amount
		self.rate=rate
		self.action=action
		self.transaction=transaction