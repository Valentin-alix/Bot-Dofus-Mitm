from com.ankamagames.dofus.enums.ActionIds import ActionIds
from com.ankamagames.dofus.datacenter.effects.EffectInstance import EffectInstance
from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.StorageGenericView import (
    StorageGenericView,
)
from com.ankamagames.dofus.types.enums.ItemCategoryEnum import ItemCategoryEnum
from com.ankamagames.jerakine.data.I18n import I18n


class StorageMinoukiView(StorageGenericView):
    def __init__(self):
        pass

    @property
    def name(self) -> str:
        return "storageMinouki"

    def isListening(self, item: ItemWrapper) -> bool:
        return (
            super().isListening(item)
            and item.category == ItemCategoryEnum.RESOURCES_CATEGORY
            and item.typeId == ItemCategoryEnum.ECAFLIP_CARD_CATEGORY
        )

    def updateView(self) -> None:
        super().updateView()

    #   if StorageOptionManager().currentStorageView == self:
    #      _hookLock.addHook(InventoryHookList.StorageViewContent,[content,InventoryManager().inventory.kamas])

    def addItem(
        self, item: ItemWrapper, invisible: int, needUpdateView: bool = True
    ) -> None:
        type: int = 0
        clone: ItemWrapper = item.clone()
        clone.quantity -= invisible
        self._content.remove(clone)
        if self._sortedContent:
            self._sortedContent = [clone] + self._sortedContent
        cardTypes: list = self.getMinoukiCardTypes(item)
        for type in cardTypes:
            if self._typesQty.get(type) and self._typesQty[type] > 0:
                self._typesQty[type] += 1
            else:
                self._typesQty[type] = 1
                self._types[type] = {
                    "name": I18n.getUiText("ui.customEffect." + type),
                    "id": type,
                }
        if needUpdateView:
            self.updateView()

    def removeItem(self, item: ItemWrapper, invisible: int) -> None:
        effect: EffectInstance = None
        idx: int = self.getItemIndex(item)
        if idx == -1:
            return
        for effect in item.possibleEffects:
            if effect.effectId == ActionIds.ACTION_ITEM_CUSTOM_EFFECT:
                if (
                    self._typesQty[effect.parameter2]
                    and self._typesQty[effect.parameter2] > 0
                ):
                    self._typesQty[effect.parameter2]-=1
                    if self._typesQty[effect.parameter2] == 0:
                        del self._types[effect.parameter2]
        self._content.splice(idx, 1)
        if self._sortedContent:
            idx = self.getItemIndex(item, self._sortedContent)
            if idx != -1:
                self._sortedContent.splice(idx, 1)
        self.updateView()

    def getMinoukiCardTypes(self, item: ItemWrapper) -> list:
        effect: EffectInstance = None
        types: list = []
        for effect in item.possibleEffects:
            if effect.effectId == ActionIds.ACTION_ITEM_CUSTOM_EFFECT:
                types.append(effect.parameter2)
        return types
