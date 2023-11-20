from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryEntryPlayerInfo import JobCrafterDirectoryEntryPlayerInfo
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectoryEntryJobInfo import JobCrafterDirectoryEntryJobInfo
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
class JobCrafterDirectoryEntryMessage:
	def __init__(self, playerInfo:JobCrafterDirectoryEntryPlayerInfo, jobInfoList:list[JobCrafterDirectoryEntryJobInfo], playerLook:EntityLook):
		self.playerInfo=playerInfo
		self.jobInfoList=jobInfoList
		self.playerLook=playerLook