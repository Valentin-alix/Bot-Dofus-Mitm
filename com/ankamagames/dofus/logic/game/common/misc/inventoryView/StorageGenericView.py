from com.ankamagames.dofus.datacenter.items.Item import Item
from com.ankamagames.dofus.internalDatacenter.DataEnum import DataEnum
from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
from com.ankamagames.dofus.kernel.Kernel import Kernel
from com.ankamagames.dofus.logic.game.common.frames.AveragePricesFrame import (
    AveragePricesFrame,
)
import com.ankamagames.dofus.logic.game.common.managers.StorageOptionManager as storageoptmgr
from com.ankamagames.dofus.logic.game.common.misc.IStorageView import IStorageView
from com.ankamagames.jerakine.logger.Logger import Logger

logger = Logger(__name__)


class StorageGenericView(IStorageView):

    _content: list[ItemWrapper]

    _sortedContent: list[ItemWrapper]

    _sorted: bool = False

    _sortFieldsCache: list

    _sortRevertCache: bool

    _typesQty: dict

    _types: dict

    def __init__(self):
        self._typesQty = dict()
        self._types = dict()
        super().__init__()

    def initialize(self, items: list[ItemWrapper]) -> None:
        item: ItemWrapper = None
        if not self._content:
            self._content = list[ItemWrapper]()
        else:
            self._content.clear()
        self._typesQty = dict()
        self._types = dict()
        self._sortedContent = None
        for item in items:
            if self.isListening(item):
                self.addItem(item, 0, False)
        self._content.sort(self.sortItemsByIndex)
        self.updateView()

    @property
    def name(self) -> str:
        raise Exception("StorageGenericView class must be extended")

    @property
    def content(self) -> list[ItemWrapper]:
        if self._sorted:
            return self._sortedContent
        return self._content

    @property
    def types(self) -> dict:
        return self._types

    def addItem(
        self, item: ItemWrapper, invisible: int, needUpdateView: bool = True
    ) -> None:
        clone: ItemWrapper = item.clone()
        clone.quantity -= invisible
        self._content.unshift(clone)
        if self._sortedContent:
            self._sortedContent.unshift(clone)
        if self._typesQty[item.typeId] and self._typesQty[item.typeId] > 0:
            ++self._typesQty[item.typeId]
        else:
            self._typesQty[item.typeId] = 1
            self._types[item.typeId] = item.type
        if needUpdateView:
            self.updateView()

    def removeItem(self, item: ItemWrapper, invisible: int) -> None:
        idx: int = self.getItemIndex(item)
        if idx == -1:
            return
        if self._typesQty[item.typeId] and self._typesQty[item.typeId] > 0:
            --self._typesQty[item.typeId]
            if self._typesQty[item.typeId] == 0:
                del self._types[item.typeId]
        self._content.splice(idx, 1)
        if self._sortedContent:
            idx = self.getItemIndex(item, self._sortedContent)
            if idx != -1:
                self._sortedContent.splice(idx, 1)
        self.updateView()

    def modifyItem(
        self, item: ItemWrapper, oldItem: ItemWrapper, invisible: int
    ) -> None:
        iw: ItemWrapper = None
        idx: int = self.getItemIndex(item)
        if idx != -1:
            iw = self._content[idx]
            if iw.quantity == item.quantity - invisible:
                iw.update(
                    item.position,
                    item.objectUID,
                    item.objectGID,
                    iw.quantity,
                    item.effectsList,
                )
                self.updateView()
            elif item.quantity <= invisible:
                self.removeItem(iw, invisible)
            else:
                iw.update(
                    item.position,
                    item.objectUID,
                    item.objectGID,
                    item.quantity - invisible,
                    item.effectsList,
                )
                self.updateView()
        elif invisible < item.quantity:
            self.addItem(item, invisible)

    def isListening(self, item: ItemWrapper) -> bool:
        return (
            item.position == 63
            and Item.getItemById(item.objectGID).typeId != DataEnum.ITEM_TYPE_HIDDEN
        )

    def getItemTypes(self) -> dict:
        return self._types

    def getItemIndex(self, item: ItemWrapper, iwlist: list[ItemWrapper] = None) -> int:
        iw: ItemWrapper = None
        if iwlist is None:
            iwlist = self._content
        for i, iw in enumerate(iwlist):
            if iw.objectUID == item.objectUID:
                return i
        return -1

    def sortItemsByIndex(self, a: ItemWrapper, b: ItemWrapper) -> int:
        if a.sortOrder > b.sortOrder:
            return -1
        if a.sortOrder == b.sortOrder:
            return 0
        return 1

    def compareFunction(
        self, a: ItemWrapper, b: ItemWrapper, sortDepth: int = 0
    ) -> int:
        returnValue: int = 0
        if self._sortFieldsCache[sortDepth] == storageoptmgr.StorageOptionManager.SORT_FIELD_NAME:
            if not self._sortRevertCache:
                returnValue = (
                    1
                    if a.nameWithoutAccent > b.nameWithoutAccent
                    else (-1 if a.nameWithoutAccent < b.nameWithoutAccent else 0)
                )
            else:
                returnValue = (
                    1
                    if a.nameWithoutAccent < b.nameWithoutAccent
                    else (-1 if a.nameWithoutAccent > b.nameWithoutAccent else 0)
                )
        if self._sortFieldsCache[sortDepth] == storageoptmgr.StorageOptionManager.SORT_FIELD_WEIGHT:
            if not self._sortRevertCache:
                returnValue = (
                    1 if a.weight < b.weight else (-1 if a.weight > b.weight else 0)
                )
            else:
                returnValue = (
                    1 if a.weight > b.weight else (-1 if a.weight < b.weight else 0)
                )
        if (
            self._sortFieldsCache[sortDepth]
            == storageoptmgr.StorageOptionManager.SORT_FIELD_LOT_WEIGHT
        ):
            if not self._sortRevertCache:
                returnValue = (
                    1
                    if a.weight * a.quantity < b.weight * b.quantity
                    else (-1 if a.weight * a.quantity > b.weight * b.quantity else 0)
                )
            else:
                returnValue = (
                    1
                    if a.weight * a.quantity > b.weight * b.quantity
                    else (-1 if a.weight * a.quantity < b.weight * b.quantity else 0)
                )
        if self._sortFieldsCache[sortDepth] == storageoptmgr.StorageOptionManager.SORT_FIELD_QUANTITY:
            if not self._sortRevertCache:
                returnValue = (
                    1
                    if a.quantity < b.quantity
                    else (-1 if a.quantity > b.quantity else 0)
                )
            else:
                returnValue = (
                    1
                    if a.quantity > b.quantity
                    else (-1 if a.quantity < b.quantity else 0)
                )
        if self._sortFieldsCache[sortDepth] == storageoptmgr.StorageOptionManager.SORT_FIELD_DEFAULT:
            if not self._sortRevertCache:
                returnValue = (
                    1
                    if a.objectUID < b.objectUID
                    else (-1 if a.objectUID > b.objectUID else 0)
                )
            else:
                returnValue = (
                    1
                    if a.objectUID > b.objectUID
                    else (-1 if a.objectUID < b.objectUID else 0)
                )
        if (
            self._sortFieldsCache[sortDepth]
            == storageoptmgr.StorageOptionManager.SORT_FIELD_AVERAGEPRICE
        ):
            if not self._sortRevertCache:
                returnValue = (
                    1
                    if self.getItemAveragePrice(a.objectGID)
                    < self.getItemAveragePrice(b.objectGID)
                    else (
                        -1
                        if self.getItemAveragePrice(a.objectGID)
                        > self.getItemAveragePrice(b.objectGID)
                        else 0
                    )
                )
            else:
                returnValue = (
                    1
                    if self.getItemAveragePrice(a.objectGID)
                    > self.getItemAveragePrice(b.objectGID)
                    else (
                        -1
                        if self.getItemAveragePrice(a.objectGID)
                        < self.getItemAveragePrice(b.objectGID)
                        else 0
                    )
                )
        if (
            self._sortFieldsCache[sortDepth]
            == storageoptmgr.StorageOptionManager.SORT_FIELD_LOT_AVERAGEPRICE
        ):
            if not self._sortRevertCache:
                returnValue = (
                    1
                    if self.getItemAveragePrice(a.objectGID) * a.quantity
                    < self.getItemAveragePrice(b.objectGID) * b.quantity
                    else (
                        -1
                        if self.getItemAveragePrice(a.objectGID) * a.quantity
                        > self.getItemAveragePrice(b.objectGID) * b.quantity
                        else 0
                    )
                )
            else:
                returnValue = (
                    1
                    if self.getItemAveragePrice(a.objectGID) * a.quantity
                    > self.getItemAveragePrice(b.objectGID) * b.quantity
                    else (
                        -1
                        if self.getItemAveragePrice(a.objectGID) * a.quantity
                        < self.getItemAveragePrice(b.objectGID) * b.quantity
                        else 0
                    )
                )
        if self._sortFieldsCache[sortDepth] == storageoptmgr.StorageOptionManager.SORT_FIELD_LEVEL:
            if not self._sortRevertCache:
                returnValue = (
                    1 if a.level < b.level else (-1 if a.level > b.level else 0)
                )
            else:
                returnValue = (
                    1 if a.level > b.level else (-1 if a.level < b.level else 0)
                )
        if (
            self._sortFieldsCache[sortDepth]
            == storageoptmgr.StorageOptionManager.SORT_FIELD_ITEM_TYPE
        ):
            if not self._sortRevertCache:
                returnValue = (
                    1
                    if a.type.name > b.type.name
                    else (-1 if a.type.name < b.type.name else 0)
                )
            else:
                returnValue = (
                    1
                    if a.type.name < b.type.name
                    else (0 if a.type.name > b.type.name else 0)
                )
        else:
            returnValue = 0
        if returnValue != 0:
            return returnValue
        if sortDepth == len(self._sortFieldsCache) - 1:
            return 0
        return self.compareFunction(a, b, sortDepth + 1)

    def getItemAveragePrice(self, pItemGID: int) -> float:
        avgPricesFrame: AveragePricesFrame = (
            Kernel().getWorker().getFrame(AveragePricesFrame)
        )
        return (
            float(avgPricesFrame.pricesData.items[pItemGID])
            if avgPricesFrame.pricesData.items.get(pItemGID) is not None
            else 0
        )

    def updateView(self) -> None:
        sameSort: bool = True
        if self._sortFieldsCache and len(self._sortFieldsCache) == len(
            self.sortFields()
        ):
            llen = len(self._sortFieldsCache)
            for i in range(llen):
                if self._sortFieldsCache[i] != self.sortFields()[i]:
                    sameSort = False
                    break
        else:
            sameSort = False
        self._sortFieldsCache = self.sortFields()
        if self._sortFieldsCache[0] != storageoptmgr.StorageOptionManager.SORT_FIELD_NONE:
            if not sameSort:
                self._sortRevertCache = self.sortRevert()
            elif storageoptmgr.StorageOptionManager().newSort:
                self._sortRevertCache = not self._sortRevertCache
            if not self._sortedContent:
                self._sortedContent = list[ItemWrapper]()
                for iw in self._content:
                    self._sortedContent.append(iw)
            self._sortedContent.sort(self.compareFunction)
            self._sorted = True
        else:
            self._sorted = False

    def sortFields(self) -> list:
        return storageoptmgr.StorageOptionManager().sortFields

    def sortRevert(self) -> bool:
        return storageoptmgr.StorageOptionManager().sortRevert

    def empty(self) -> None:
        self._content = list[ItemWrapper]()
        self._sortedContent = None
        self.updateView()
