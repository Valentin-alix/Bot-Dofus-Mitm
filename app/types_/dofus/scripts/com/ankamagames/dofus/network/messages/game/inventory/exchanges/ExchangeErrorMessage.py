from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ExchangeErrorMessage:
	def __init__(self, errorType:int):
		self.errorType=errorType