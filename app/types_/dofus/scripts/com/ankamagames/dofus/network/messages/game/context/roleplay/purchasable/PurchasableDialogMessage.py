from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class PurchasableDialogMessage:
	def __init__(self, purchasableId:float, purchasableInstanceId:int, price:int):
		self.purchasableId=purchasableId
		self.purchasableInstanceId=purchasableInstanceId
		self.price=price