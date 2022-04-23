from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
from com.ankamagames.dofus.logic.game.common.misc.IInventoryView import IInventoryView
from com.ankamagames.jerakine.logger.Logger import Logger

logger = Logger(__name__)


class ListView(IInventoryView):
    _view: list[ItemWrapper]

    def __init__(self):
        self._view = list[ItemWrapper]()
        super().__init__()

    @property
    def name(self) -> str:
        raise Exception("get name() is abstract method, it should be implemented")

    def initialize(self, items: list[ItemWrapper]) -> None:
        item: ItemWrapper = None
        self._view.splice(0, len(self._view))
        for item in items:
            self._view.append(item)
        self.updateView()

    @property
    def content(self) -> list[ItemWrapper]:
        return self._view

    def addItem(
        self, item: ItemWrapper, invisible: int, needUpdateView: bool = True
    ) -> None:
        self._view.append(item)

    def removeItem(self, item: ItemWrapper, invisible: int) -> None:
        i: int = self._view.find(item)
        if i == -1:
            raise Exception(
                "Demande de suppression d'un item (id "
                + item.objectUID
                + ") qui n'existe pas dans la vue "
                + self.name
            )
        self._view.splice(i, 1)

    def modifyItem(
        self, item: ItemWrapper, oldItem: ItemWrapper, invisible: int
    ) -> None:
        i: int = self._view.find(item)
        if i == -1:
            raise Exception(
                "Demande de modification d'un item (id "
                + item.objectUID
                + ") qui n'existe pas dans la vue "
                + self.name
            )
        self._view[i] = item

    def isListening(self, item: ItemWrapper) -> bool:
        raise Exception("isListening() is abstract method, it should be implemented")

    def updateView(self) -> None:
        raise Exception("updateView() is abstract method, it should be implemented")

    def empty(self) -> None:
        self._view = list[ItemWrapper]()
        self.updateView()
