from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.StorageGenericView import (
    StorageGenericView,
)
from com.ankamagames.dofus.types.enums.ItemCategoryEnum import ItemCategoryEnum


class StorageConsumablesView(StorageGenericView):
    def __init__(self):
        super().__init__()

    @property
    def name(self) -> str:
        return "storageConsumables"

    def isListening(self, item: ItemWrapper) -> bool:
        return (
            super().isListening(item)
            and item.category == ItemCategoryEnum.CONSUMABLES_CATEGORY
        )

    def updateView(self) -> None:
        super().updateView()
