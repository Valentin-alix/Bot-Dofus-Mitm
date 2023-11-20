from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class MapObstacle:
	def __init__(self, obstacleCellId:int, state:int):
		self.obstacleCellId=obstacleCellId
		self.state=state