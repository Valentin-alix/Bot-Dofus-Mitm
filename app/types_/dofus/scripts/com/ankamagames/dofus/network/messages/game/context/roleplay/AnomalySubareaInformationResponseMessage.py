from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.AnomalySubareaInformation import AnomalySubareaInformation
class AnomalySubareaInformationResponseMessage:
	def __init__(self, subareas:list[AnomalySubareaInformation]):
		self.subareas=subareas