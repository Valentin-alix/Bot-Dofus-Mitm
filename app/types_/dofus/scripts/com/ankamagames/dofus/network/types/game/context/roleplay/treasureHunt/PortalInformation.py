from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class PortalInformation:
	def __init__(self, portalId:int, areaId:int):
		self.portalId=portalId
		self.areaId=areaId