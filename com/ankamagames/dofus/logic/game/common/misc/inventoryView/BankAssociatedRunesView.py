from com.ankamagames.dofus.datacenter.effects.Effect import Effect
from com.ankamagames.dofus.datacenter.effects.EffectInstance import EffectInstance
from com.ankamagames.dofus.internalDatacenter.DataEnum import DataEnum
from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
import com.ankamagames.dofus.logic.game.common.managers.StorageOptionManager as storageoptmgr
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.StorageGenericView import (
    StorageGenericView,
)


class BankAssociatedRunesView(StorageGenericView):

    _item: ItemWrapper

    def __init__(self, item: ItemWrapper):
        self._item = item

    def initialize(self, items: list[ItemWrapper]) -> None:
        item: ItemWrapper = None
        tempContent: list[ItemWrapper] = list[ItemWrapper]()
        for item in items:
            if self.isListening(item):
                tempContent.append(item)
        if len(tempContent) > 0:
            self._content = list[ItemWrapper]()
            self._sortedContent = list[ItemWrapper]()
            for item in tempContent:
                self.addItem(item, 0, False)

    @property
    def name(self) -> str:
        return "bankAssociatedRunes"

    def isListening(self, rune: ItemWrapper) -> bool:
        itemEffects: list[EffectInstance] = self._item.effects.extend(
            self._item.possibleEffects
        )
        if rune.typeId != DataEnum.ITEM_TYPE_SMITHMAGIC_RUNE:
            return False
        runeEffects = rune.effects.extend(rune.possibleEffects)
        for itemEffect in itemEffects:
            for runeEffect in runeEffects:
                if (
                    Effect.getEffectById(itemEffect.effectId).characteristic
                    == Effect.getEffectById(runeEffect.effectId).characteristic
                ):
                    return True
        return False

    def addItem(
        self, item: ItemWrapper, invisible: int, needUpdateView: bool = True
    ) -> None:
        super().addItem(item, invisible, needUpdateView)

    def modifyItem(
        self, item: ItemWrapper, oldItem: ItemWrapper, invisible: int
    ) -> None:
        super().modifyItem(item, oldItem, invisible)

    def updateView(self) -> None:
        super().updateView()

    def sortFields(self) -> list:
        return storageoptmgr.StorageOptionManager().sortBankFields

    def sortRevert(self) -> bool:
        return storageoptmgr.StorageOptionManager().sortBankRevert
