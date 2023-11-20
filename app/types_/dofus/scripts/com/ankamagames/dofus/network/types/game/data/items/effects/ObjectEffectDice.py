from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
if TYPE_CHECKING:
	...
class ObjectEffectDice(ObjectEffect):
	def __init__(self, diceNum:int, diceSide:int, diceConst:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.diceNum=diceNum
		self.diceSide=diceSide
		self.diceConst=diceConst