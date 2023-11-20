from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class KohAllianceRoleMembers:
	def __init__(self, memberCount:int, roleAvAId:int):
		self.memberCount=memberCount
		self.roleAvAId=roleAvAId