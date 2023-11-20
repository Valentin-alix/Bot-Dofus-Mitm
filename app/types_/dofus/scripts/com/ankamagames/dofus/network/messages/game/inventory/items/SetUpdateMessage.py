from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
class SetUpdateMessage:
	def __init__(self, setId:int, setObjects:list[int], setEffects:list[ObjectEffect]):
		self.setId=setId
		self.setObjects=setObjects
		self.setEffects=setEffects