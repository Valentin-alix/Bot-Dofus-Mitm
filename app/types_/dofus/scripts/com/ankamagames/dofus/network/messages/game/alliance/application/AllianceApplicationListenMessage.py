from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AllianceApplicationListenMessage:
	def __init__(self, listen:bool):
		self.listen=listen