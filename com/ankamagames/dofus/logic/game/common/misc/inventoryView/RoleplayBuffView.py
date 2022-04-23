from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
from com.ankamagames.dofus.logic.game.common.misc.IInventoryView import IInventoryView
from com.ankamagames.dofus.network.enums.CharacterInventoryPositionEnum import (
    CharacterInventoryPositionEnum,
)
from com.ankamagames.jerakine.logger.Logger import Logger

logger = Logger(__name__)


class RoleplayBuffView(IInventoryView):

    _content: list[ItemWrapper]

    def __init__(self):
        super().__init__()

    def initialize(self, items: list[ItemWrapper]) -> None:
        item: ItemWrapper = None
        self._content = list[ItemWrapper]()
        for item in items:
            if self.isListening(item):
                self.addItem(item, 0, False)
        self.updateView()

    @property
    def name(self) -> str:
        return "roleplayBuff"

    @property
    def content(self) -> list[ItemWrapper]:
        return self._content

    def addItem(
        self, item: ItemWrapper, invisible: int, needUpdateView: bool = True
    ) -> None:
        self._content.unshift(item)
        if needUpdateView:
            self.updateView()

    def removeItem(self, item: ItemWrapper, invisible: int) -> None:
        idx: int = self.content.find(item)
        if idx == -1:
            logger.warn("L'item qui doit �tre supprim� n'est pas pr�sent dans la liste")
        self.content.splice(idx, 1)
        self.updateView()

    def modifyItem(
        self, item: ItemWrapper, oldItem: ItemWrapper, invisible: int
    ) -> None:
        self.updateView()

    def isListening(self, item: ItemWrapper) -> bool:
        return (
            item.position == CharacterInventoryPositionEnum.INVENTORY_POSITION_MUTATION
            or item.position
            == CharacterInventoryPositionEnum.INVENTORY_POSITION_BOOST_FOOD
            or item.position
            == CharacterInventoryPositionEnum.INVENTORY_POSITION_FIRST_BONUS
            or item.position
            == CharacterInventoryPositionEnum.INVENTORY_POSITION_SECOND_BONUS
            or item.position
            == CharacterInventoryPositionEnum.INVENTORY_POSITION_FIRST_MALUS
            or item.position
            == CharacterInventoryPositionEnum.INVENTORY_POSITION_SECOND_MALUS
            or item.position
            == CharacterInventoryPositionEnum.INVENTORY_POSITION_ROLEPLAY_BUFFER
            or item.position
            == CharacterInventoryPositionEnum.INVENTORY_POSITION_FOLLOWER
        )

    def updateView(self) -> None:
        pass

    def empty(self) -> None:
        self._content = list[ItemWrapper]()
        self.updateView()
