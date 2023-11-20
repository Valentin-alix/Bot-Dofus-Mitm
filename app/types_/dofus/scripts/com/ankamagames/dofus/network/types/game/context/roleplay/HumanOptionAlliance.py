from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformation import AllianceInformation
class HumanOptionAlliance(HumanOption):
	def __init__(self, allianceInformation:AllianceInformation, aggressable:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.allianceInformation=allianceInformation
		self.aggressable=aggressable