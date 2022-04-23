from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
from com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager import (
    PlayedCharacterManager,
)
from com.ankamagames.dofus.logic.game.common.misc.IInventoryView import IInventoryView
from com.ankamagames.dofus.network.enums.CharacterInventoryPositionEnum import (
    CharacterInventoryPositionEnum,
)
from com.ankamagames.jerakine.logger.Logger import Logger

logger = Logger(__name__)


class EquipmentView(IInventoryView):

    _content: list[ItemWrapper]

    _initializing: bool

    def __init__(self):
        self._content = list[ItemWrapper]()
        super().__init__()

    def initialize(self, items: list[ItemWrapper]) -> None:
        self._content = list[ItemWrapper]()
        PlayedCharacterManager().currentWeapon = None
        for item in items:
            if self.isListening(item):
                self.addItem(item, 0)
            if (
                item.position
                == CharacterInventoryPositionEnum.ACCESSORY_POSITION_WEAPON
            ):
                PlayedCharacterManager().currentWeapon = item
        self._initializing = False

    @property
    def name(self) -> str:
        return "equipment"

    @property
    def content(self) -> list[ItemWrapper]:
        return self._content

    def addItem(
        self, item: ItemWrapper, invisible: int, needUpdateView: bool = True
    ) -> None:
        self.content[item.position] = item
        if item.position == CharacterInventoryPositionEnum.ACCESSORY_POSITION_WEAPON:
            PlayedCharacterManager().currentWeapon = item
        if not self._initializing:
            pass

    def removeItem(self, item: ItemWrapper, invisible: int) -> None:
        self.content[item.position] = None
        if item.position == CharacterInventoryPositionEnum.ACCESSORY_POSITION_WEAPON:
            PlayedCharacterManager().currentWeapon = None

    def modifyItem(
        self, item: ItemWrapper, oldItem: ItemWrapper, invisible: int
    ) -> None:
        if self.content[oldItem.position] == item:
            self.content[oldItem.position] = None
        self.content[item.position] = item
        if item.position == CharacterInventoryPositionEnum.ACCESSORY_POSITION_WEAPON:
            pass

    def isListening(self, item: ItemWrapper) -> bool:
        return item.position <= 61

    def updateView(self) -> None:
        pass

    def empty(self) -> None:
        pass
