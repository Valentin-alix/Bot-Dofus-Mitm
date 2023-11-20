from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.common.basic.BasicStatMessage import BasicStatMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.common.basic.StatisticData import StatisticData
class BasicStatWithDataMessage(BasicStatMessage):
	def __init__(self, datas:list[StatisticData], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.datas=datas