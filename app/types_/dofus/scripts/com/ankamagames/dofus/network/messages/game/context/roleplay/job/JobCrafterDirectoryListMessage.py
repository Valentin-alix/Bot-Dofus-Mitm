from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryListEntry import JobCrafterDirectoryListEntry
class JobCrafterDirectoryListMessage:
	def __init__(self, listEntries:list[JobCrafterDirectoryListEntry]):
		self.listEntries=listEntries