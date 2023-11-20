from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.look.SubEntity import SubEntity
class EntityLook:
	def __init__(self, bonesId:int, skins:list[int], indexedColors:list[int], scales:list[int], subentities:list[SubEntity]):
		self.bonesId=bonesId
		self.skins=skins
		self.indexedColors=indexedColors
		self.scales=scales
		self.subentities=subentities