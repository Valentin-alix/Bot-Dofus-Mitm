from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
from com.ankamagames.dofus.logic.game.common.managers.StorageOptionManager import (
    StorageOptionManager,
)
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.StorageGenericView import (
    StorageGenericView,
)


class StorageFilteredView(StorageGenericView):
    def __init__(self):
        super().__init__()

    @property
    def name(self) -> str:
        return "storageFiltered"

    def isListening(self, item: ItemWrapper) -> bool:
        return (
            super().isListening(item)
            and StorageOptionManager().hasFilter()
            and item.typeId == StorageOptionManager().filter
        )

    def updateView(self) -> None:
        super().updateView()
