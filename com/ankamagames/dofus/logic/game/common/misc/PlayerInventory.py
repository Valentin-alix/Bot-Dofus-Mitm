from com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager import (
    PlayedCharacterManager,
)
from com.ankamagames.dofus.logic.game.common.misc.Inventory import Inventory


class PlayerInventory(Inventory):
    def __init__(self):
        super().__init__()
        
    @property
    def kamas(self):
        raise RuntimeError('This property has no getter!')
    
    @kamas.setter
    def kamas(self, value: float) -> None:
        if PlayedCharacterManager().characteristics:
            PlayedCharacterManager().characteristics.kamas = value
        super().kamas = value
