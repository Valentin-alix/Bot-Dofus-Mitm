from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class TrustCertificate:
	def __init__(self, id:int, hash:str):
		self.id=id
		self.hash=hash