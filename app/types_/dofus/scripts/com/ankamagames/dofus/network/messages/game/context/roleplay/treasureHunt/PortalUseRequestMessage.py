from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class PortalUseRequestMessage:
	def __init__(self, portalId:int):
		self.portalId=portalId