from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.job.JobCrafterDirectorySettings import JobCrafterDirectorySettings
class JobCrafterDirectorySettingsMessage:
	def __init__(self, craftersSettings:list[JobCrafterDirectorySettings]):
		self.craftersSettings=craftersSettings