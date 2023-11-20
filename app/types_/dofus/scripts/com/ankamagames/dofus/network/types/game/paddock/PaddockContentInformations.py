from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.paddock.PaddockInformations import PaddockInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.paddock.MountInformationsForPaddock import MountInformationsForPaddock
class PaddockContentInformations(PaddockInformations):
	def __init__(self, paddockId:float, worldX:int, worldY:int, mapId:float, subAreaId:int, abandonned:bool, mountsInformations:list[MountInformationsForPaddock], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.paddockId=paddockId
		self.worldX=worldX
		self.worldY=worldY
		self.mapId=mapId
		self.subAreaId=subAreaId
		self.abandonned=abandonned
		self.mountsInformations=mountsInformations