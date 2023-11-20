from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ExchangeStartOkJobIndexMessage:
	def __init__(self, jobs:list[int]):
		self.jobs=jobs