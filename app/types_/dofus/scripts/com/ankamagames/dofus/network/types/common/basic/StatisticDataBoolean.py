from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.common.basic.StatisticData import StatisticData
if TYPE_CHECKING:
	...
class StatisticDataBoolean(StatisticData):
	def __init__(self, value:bool, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.value=value