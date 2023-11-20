from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartOkMountWithOutPaddockMessage import ExchangeStartOkMountWithOutPaddockMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.mount.MountClientData import MountClientData
class ExchangeStartOkMountMessage(ExchangeStartOkMountWithOutPaddockMessage):
	def __init__(self, paddockedMountsDescription:list[MountClientData], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.paddockedMountsDescription=paddockedMountsDescription