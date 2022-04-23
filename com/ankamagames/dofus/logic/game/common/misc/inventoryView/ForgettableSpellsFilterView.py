from com.ankamagames.dofus.datacenter.items.Item import Item
from com.ankamagames.dofus.datacenter.optionalFeatures.ForgettableSpell import (
    ForgettableSpell,
)
from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper

from com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager import (
    PlayedCharacterManager,
)

from com.ankamagames.dofus.logic.game.common.misc.IStorageView import IStorageView
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.StorageGenericView import (
    StorageGenericView,
)


class ForgettableSpellsFilterView(StorageGenericView):

    _allowedTypes: list[int]

    _parent: IStorageView

    _isHideLearnedSpells: bool = False

    def __init__(
        self,
        parentView: IStorageView,
        allowedTypes: list[int],
        isHideLearnedSpells: bool,
    ):
        super().__init__()
        self._allowedTypes = allowedTypes
        self._parent = parentView
        self._isHideLearnedSpells = isHideLearnedSpells

    @property
    def name(self) -> str:
        return "forgettableSpellsFilter"

    def isListening(self, item: ItemWrapper) -> bool:
        if self._parent is None:
            return False
        data: Item = Item.getItemById(item.objectGID)
        return bool(
            self._parent.isListening(item)
            and super().isListening(item)
            and data.typeId in self._allowedTypes
        )

    def addItem(
        self, item: ItemWrapper, invisible: int, needUpdateView: bool = True
    ) -> None:
        if item is not None and self.isItemFiltered(item.id):
            return
        super().addItem(item, invisible, needUpdateView)

    def modifyItem(
        self, item: ItemWrapper, oldItem: ItemWrapper, invisible: int
    ) -> None:
        if item is not None and self.isItemFiltered(item.id):
            return
        super().modifyItem(item, oldItem, invisible)

    def updateView(self) -> None:
        super().updateView()

    @property
    def parent(self) -> IStorageView:
        return self._parent

    @parent.setter
    def parent(self, view: IStorageView) -> None:
        self._parent = view

    def isItemFiltered(self, scrollId: int) -> bool:
        playerForgettableSpells: dict = None
        if not self._isHideLearnedSpells:
            return False
        forgettableSpell: ForgettableSpell = (
            ForgettableSpell.getForgettableSpellByScrollId(scrollId)
        )
        if forgettableSpell is not None:
            playerForgettableSpells = (
                PlayedCharacterManager().playerForgettableSpelldict
            )
            if forgettableSpell.id in playerForgettableSpells:
                return True
        return False
