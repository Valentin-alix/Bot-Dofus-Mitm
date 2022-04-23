from com.ankamagames.dofus.internalDatacenter.DataEnum import DataEnum
from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.StorageGenericView import (
    StorageGenericView,
)
from com.ankamagames.dofus.types.enums.ItemCategoryEnum import ItemCategoryEnum


class StorageResourcesView(StorageGenericView):
    def __init__(self):
        super().__init__()

    @property
    def name(self) -> str:
        return "storageResources"

    def isListening(self, item: ItemWrapper) -> bool:
        return (
            super().isListening(item)
            and item.category == ItemCategoryEnum.RESOURCES_CATEGORY
            and item.typeId != DataEnum.ITEM_TYPE_ECAFLIP_CARD
        )

    def updateView(self) -> None:
        super().updateView()
