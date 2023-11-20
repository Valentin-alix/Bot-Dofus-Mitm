from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.inventory.UpdatedStorageTabInformation import UpdatedStorageTabInformation
class GuildUpdateChestTabRequestMessage:
	def __init__(self, tab:UpdatedStorageTabInformation):
		self.tab=tab