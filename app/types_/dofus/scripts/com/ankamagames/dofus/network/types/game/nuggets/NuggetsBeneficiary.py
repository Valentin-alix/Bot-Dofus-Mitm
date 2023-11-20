from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class NuggetsBeneficiary:
	def __init__(self, beneficiaryPlayerId:int, nuggetsQuantity:int):
		self.beneficiaryPlayerId=beneficiaryPlayerId
		self.nuggetsQuantity=nuggetsQuantity