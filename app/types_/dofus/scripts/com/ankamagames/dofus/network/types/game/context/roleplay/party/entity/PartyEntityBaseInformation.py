from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
class PartyEntityBaseInformation:
	def __init__(self, indexId:int, entityModelId:int, entityLook:EntityLook):
		self.indexId=indexId
		self.entityModelId=entityModelId
		self.entityLook=entityLook