from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AbstractFightDispellableEffect:
	def __init__(self, uid:int, targetId:float, turnDuration:int, dispelable:int, spellId:int, effectId:int, parentBoostUid:int):
		self.uid=uid
		self.targetId=targetId
		self.turnDuration=turnDuration
		self.dispelable=dispelable
		self.spellId=spellId
		self.effectId=effectId
		self.parentBoostUid=parentBoostUid