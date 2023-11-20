from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.BasicAllianceInformations import BasicAllianceInformations
if TYPE_CHECKING:
	...
class BasicNamedAllianceInformations(BasicAllianceInformations):
	def __init__(self, allianceName:str, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.allianceName=allianceName