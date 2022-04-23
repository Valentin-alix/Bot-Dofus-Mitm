from com.ankamagames.dofus.internalDatacenter.DataEnum import DataEnum
from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
from com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager import (
    PlayedCharacterManager,
)
import com.ankamagames.dofus.logic.game.common.managers.StorageOptionManager as storageoptmgr
from com.ankamagames.dofus.logic.game.common.misc.IInventoryView import IInventoryView
from com.ankamagames.dofus.network.enums.CharacterInventoryPositionEnum import (
    CharacterInventoryPositionEnum,
)
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
from com.ankamagames.jerakine.logger.Logger import Logger

logger = Logger(__name__)


class Inventory:

    _itemsDict: dict

    _views: dict

    _kamas: float = 0

    def __init__(self):
        self._itemsDict = dict()
        super().__init__()
        self._views = dict()

    @property
    def kamas(self) -> float:
        return self._kamas

    @kamas.setter
    def kamas(self, value: float) -> None:
        self._kamas = value
        storageoptmgr.StorageOptionManager().updateStorageView()

    def addView(self, view: IInventoryView) -> None:
        self._views[view.name] = view

    def getView(self, name: str) -> IInventoryView:
        return self._views[name]

    def removeView(self, name: str) -> None:
        view: IInventoryView = self.getView(name)
        if view:
            del self._views[name]

    def getItem(self, uid: int) -> ItemWrapper:
        if self._itemsDict[uid]:
            return self._itemsDict[uid].item
        return None

    def getItemMaskCount(self, uid: int, mask: str) -> int:
        itemSet: ItemSet = self._itemsDict[uid]
        if not itemSet:
            logger.error("Suppression d'un item qui n'existe pas")
            return 0
        if itemSet.masks.hasOwnProperty(mask):
            return itemSet.masks[mask]
        return 0

    def initialize(self, items: list[ItemWrapper]) -> None:
        item: ItemWrapper = None
        itemSet: ItemSet = None
        self._itemsDict = dict()
        for item in items:
            itemSet = ItemSet(item)
            self._itemsDict[item.objectUID] = itemSet
        self.initializeViews(items)

    def initializeFromObjectItems(self, items: list[ObjectItem]) -> None:
        self._itemsDict = dict()
        iteml: iteml[ItemWrapper] = iteml[ItemWrapper]()
        l: int = len(items)
        for i in range(l):
            item = items[i]
            iw = ItemWrapper.create(
                item.position,
                item.objectUID,
                item.objectGID,
                item.quantity,
                item.effects,
            )
            self._itemsDict[item.objectUID] = ItemSet(iw)
            iteml.append(iw)
        self.initializeViews(iteml)

    def addObjectItem(self, item: ObjectItem) -> None:
        iw: ItemWrapper = ItemWrapper.create(
            item.position,
            item.objectUID,
            item.objectGID,
            item.quantity,
            item.effects,
            False,
        )
        self.addItem(iw)

    def addItem(self, item: ItemWrapper) -> None:
        itemSet: ItemSet = self._itemsDict[item.objectUID]
        if itemSet:
            oldItem = item.clone()
            itemSet.item.quantity += item.quantity
            itemSet.masks = dict()
            self.modifyItemFromViews(itemSet, oldItem)
        else:
            itemSet = ItemSet(item)
            self._itemsDict[item.objectUID] = itemSet
            self.addItemToViews(itemSet)

    def removeItem(self, itemUID: int, quantity: int = -1) -> None:
        oldItem: ItemWrapper = None
        itemSet: ItemSet = self._itemsDict[itemUID]
        if not itemSet:
            logger.error("Suppression d'un item qui n'existe pas")
            return
        if quantity == -1 or quantity == itemSet.item.quantity:
            del self._itemsDict[itemUID]
            self.removeItemFromViews(itemSet)
        else:
            if itemSet.item.quantity < quantity:
                logger.error(
                    "On essaye de supprimer de l'inventaire plus d'objet qu'il n'en existe"
                )
                return
            oldItem = itemSet.item.clone()
            itemSet.item.quantity -= quantity
            self.modifyItemFromViews(itemSet, oldItem)

    def modifyItemQuantity(self, itemUID: int, quantity: int) -> None:
        itemSet: ItemSet = self._itemsDict[itemUID]
        if not itemSet:
            logger.error(
                "On essaye de modifier la quantit� d'un objet qui n'existe pas"
            )
            return
        iw: ItemWrapper = itemSet.item.clone()
        iw.quantity = quantity
        self.modifyItem(iw)

    def modifyItemPosition(self, itemUID: int, position: int) -> None:
        itemSet: ItemSet = self._itemsDict[itemUID]
        if not itemSet:
            logger.error(
                "On essaye de modifier la position d'un objet qui n'existe pas"
            )
            return
        iw: ItemWrapper = itemSet.item.clone()
        iw.position = position
        if iw.typeId == DataEnum.ITEM_TYPE_PETSMOUNT:
            if position == CharacterInventoryPositionEnum.ACCESSORY_POSITION_PETS:
                PlayedCharacterManager().isPetsMounting = True
                PlayedCharacterManager().petsMount = itemSet.item
            else:
                PlayedCharacterManager().isPetsMounting = False
                PlayedCharacterManager().petsMount = None
        elif iw.typeId == DataEnum.ITEM_TYPE_COMPANION:
            if position == CharacterInventoryPositionEnum.INVENTORY_POSITION_ENTITY:
                PlayedCharacterManager().hasCompanion = True
            else:
                PlayedCharacterManager().hasCompanion = False
        self.modifyItem(iw)

    def modifyObjectItem(self, item: ObjectItem) -> ItemWrapper:
        iw: ItemWrapper = ItemWrapper.create(
            item.position,
            item.objectUID,
            item.objectGID,
            item.quantity,
            item.effects,
            False,
        )
        self.modifyItem(iw)
        return iw

    def modifyItem(self, item: ItemWrapper) -> None:
        oldItem: ItemWrapper = None
        itemSet: ItemSet = self._itemsDict[item.objectUID]
        if itemSet:
            oldItem = itemSet.item.clone()
            self.copyItem(itemSet.item, item)
            self.modifyItemFromViews(itemSet, oldItem)
        else:
            self.addItem(item)

    def addItemMask(self, objectUID: int, name: str, size: int) -> None:
        itemSet: ItemSet = self._itemsDict[objectUID]
        if not itemSet:
            logger.error(
                "On essaye de masquer un item qui n'existe pas dans l'inventaire"
            )
            return
        itemSet.masks[name] = size
        self.modifyItemFromViews(itemSet, itemSet.item)

    def removeItemMask(self, objectUID: int, name: str) -> None:
        itemSet: ItemSet = self._itemsDict[objectUID]
        if not itemSet:
            return
        del itemSet.masks[name]
        self.modifyItemFromViews(itemSet, itemSet.item)

    def removeAllItemMasks(self, name: str) -> None:
        itemSet: ItemSet = None
        for itemSet in self._itemsDict:
            if itemSet.masks[name]:
                del itemSet.masks[name]
                self.modifyItemFromViews(itemSet, itemSet.item)

    def releaseHooks(self) -> None:
        self._hookLock.release()

    def refillView(self, src: str, dst: str) -> None:
        fromView: IInventoryView = self.getView(src)
        toView: IInventoryView = self.getView(dst)
        if not fromView or not toView:
            return
        toView.initialize(fromView.content)

    def addItemToViews(self, itemSet: "ItemSet") -> None:
        view: IInventoryView = None
        for view in self._views:
            if view.isListening(itemSet.item):
                view.addItem(itemSet.item, 0)

    def modifyItemFromViews(self, itemSet: "ItemSet", oldItem: ItemWrapper) -> None:
        mask: int = 0
        view: IInventoryView = None
        quantity: int = 0
        for mask in itemSet.masks:
            quantity += mask
        for view in self._views:
            if view.isListening(itemSet.item):
                if view.isListening(oldItem):
                    view.modifyItem(itemSet.item, oldItem, quantity)
                else:
                    view.addItem(itemSet.item, quantity)
            elif view.isListening(oldItem):
                view.removeItem(oldItem, quantity)

    def removeItemFromViews(self, itemSet: "ItemSet") -> None:
        view: IInventoryView = None
        for view in self._views:
            if view.isListening(itemSet.item):
                view.removeItem(itemSet.item, 0)

    def initializeViews(self, items: list[ItemWrapper]) -> None:
        view: IInventoryView = None
        for view in self._views:
            view.initialize(items)

    def copyItem(self, target: ItemWrapper, source: ItemWrapper) -> None:
        target.update(
            source.position,
            source.objectUID,
            source.objectGID,
            source.quantity,
            source.effectsList,
        )


class ItemSet:

    item: ItemWrapper

    _masks: dict

    def __init__(self, iw: ItemWrapper):
        self.item = iw

    @property
    def masks(self) -> dict:
        if not self._masks:
            self._masks = dict()
        return self._masks

    @masks.setter
    def masks(self, value: dict) -> None:
        self._masks = value
