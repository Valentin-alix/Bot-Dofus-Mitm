from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
from com.ankamagames.dofus.logic.game.common.managers.StorageOptionManager import (
    StorageOptionManager,
)
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.StorageGenericView import (
    StorageGenericView,
)
from com.ankamagames.dofus.types.enums.ItemCategoryEnum import ItemCategoryEnum


class BankEquipementView(StorageGenericView):
    def __init__(self):
        super().__init__()

    @property
    def name(self) -> str:
        return "bankEquipement"

    def isListening(self, item: ItemWrapper) -> bool:
        return (
            super().isListening(item)
            and item.category == ItemCategoryEnum.EQUIPMENT_CATEGORY
        )

    def updateView(self) -> None:
        super().updateView()

    def sortFields(self) -> list:
        return StorageOptionManager().sortBankFields

    def sortRevert(self) -> bool:
        return StorageOptionManager().sortBankRevert
