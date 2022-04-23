from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.StorageGenericView import (
    StorageGenericView,
)
from com.ankamagames.dofus.types.enums.ItemCategoryEnum import ItemCategoryEnum


class StorageCosmeticsView(StorageGenericView):
    def __init__(self):
        super().__init__()

    @property
    def name(self) -> str:
        return "storageCosmetics"

    def isListening(self, item: ItemWrapper) -> bool:
        return (
            super().isListening(item)
            and item.category == ItemCategoryEnum.COSMETICS_CATEGORY
        )

    def updateView(self) -> None:
        super().updateView()
