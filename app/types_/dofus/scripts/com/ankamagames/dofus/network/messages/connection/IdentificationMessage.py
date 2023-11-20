from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.version.Version import Version
class IdentificationMessage:
	def __init__(self, version:Version, lang:str, credentials:list[int], serverId:int, sessionOptionalSalt:int, failedAttempts:list[int]):
		self.version=version
		self.lang=lang
		self.credentials=credentials
		self.serverId=serverId
		self.sessionOptionalSalt=sessionOptionalSalt
		self.failedAttempts=failedAttempts