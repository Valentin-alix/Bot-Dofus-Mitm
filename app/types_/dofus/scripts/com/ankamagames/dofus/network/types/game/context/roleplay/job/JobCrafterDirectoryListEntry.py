from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryEntryPlayerInfo import JobCrafterDirectoryEntryPlayerInfo
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryEntryJobInfo import JobCrafterDirectoryEntryJobInfo
class JobCrafterDirectoryListEntry:
	def __init__(self, playerInfo:JobCrafterDirectoryEntryPlayerInfo, jobInfo:JobCrafterDirectoryEntryJobInfo):
		self.playerInfo=playerInfo
		self.jobInfo=jobInfo