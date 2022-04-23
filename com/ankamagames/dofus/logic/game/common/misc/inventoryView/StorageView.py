from com.ankamagames.dofus.logic.game.common.managers.StorageOptionManager import (
    StorageOptionManager,
)
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.StorageGenericView import (
    StorageGenericView,
)


class StorageView(StorageGenericView):
    def __init__(self):
        super().__init__()

    @property
    def name(self) -> str:
        return "storage"

    def updateView(self) -> None:
        super().updateView()

    def sortFields(self) -> list:
        return StorageOptionManager().sortFields

    def sortRevert(self) -> bool:
        return StorageOptionManager().sortRevert
