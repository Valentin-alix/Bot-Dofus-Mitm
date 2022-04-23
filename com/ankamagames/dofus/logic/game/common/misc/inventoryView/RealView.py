from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.ListView import ListView


class RealView(ListView):
    def __init__(self):
        super().__init__()

    @property
    def name(self) -> str:
        return "real"

    def addItem(
        self, item: ItemWrapper, invisible: int, needUpdateView: bool = True
    ) -> None:
        super().addItem(item, invisible, needUpdateView)
        if needUpdateView:
            self.updateView()

    def removeItem(self, item: ItemWrapper, invisible: int) -> None:
        super().removeItem(item, invisible)
        self.updateView()

    def modifyItem(
        self, item: ItemWrapper, oldItem: ItemWrapper, invisible: int
    ) -> None:
        super().modifyItem(item, oldItem, invisible)
        if item.quantity != oldItem.quantity:
            pass
        self.updateView()

    def isListening(self, item: ItemWrapper) -> bool:
        return True

    def updateView(self) -> None:
        pass
