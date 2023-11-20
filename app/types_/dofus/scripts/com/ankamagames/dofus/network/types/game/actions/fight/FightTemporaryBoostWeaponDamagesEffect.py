from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.actions.fight.FightTemporaryBoostEffect import FightTemporaryBoostEffect
if TYPE_CHECKING:
	...
class FightTemporaryBoostWeaponDamagesEffect(FightTemporaryBoostEffect):
	def __init__(self, weaponTypeId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.weaponTypeId=weaponTypeId