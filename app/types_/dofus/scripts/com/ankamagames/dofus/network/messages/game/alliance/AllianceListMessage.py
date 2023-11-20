from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.AllianceFactSheetInformation import AllianceFactSheetInformation
class AllianceListMessage:
	def __init__(self, alliances:list[AllianceFactSheetInformation]):
		self.alliances=alliances