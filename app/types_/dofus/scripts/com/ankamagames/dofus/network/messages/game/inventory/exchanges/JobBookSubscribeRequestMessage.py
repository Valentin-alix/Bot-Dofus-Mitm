from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class JobBookSubscribeRequestMessage:
	def __init__(self, jobIds:list[int]):
		self.jobIds=jobIds