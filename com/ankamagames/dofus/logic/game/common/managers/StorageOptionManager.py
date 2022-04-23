from com.ankamagames.dofus.datacenter.jobs.Skill import Skill
from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
from com.ankamagames.dofus.kernel.Kernel import Kernel
import com.ankamagames.dofus.logic.game.common.managers.InventoryManager as inventorymgr
from com.ankamagames.dofus.logic.game.common.misc.IInventoryView import IInventoryView
from com.ankamagames.dofus.logic.game.common.misc.IStorageView import IStorageView
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from com.ankamagames.dofus.logic.game.common.misc.Inventory import Inventory
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.BankAssociatedRunesView import (
    BankAssociatedRunesView,
)
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.ForgettableSpellsFilterView import (
    ForgettableSpellsFilterView,
)
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.StorageBidHouseFilterView import (
    StorageBidHouseFilterView,
)
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.StorageCraftFilterView import (
    StorageCraftFilterView,
)
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.StorageSmithMagicFilterView import (
    StorageSmithMagicFilterView,
)
from com.ankamagames.dofus.types.enums.ItemCategoryEnum import ItemCategoryEnum
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.metaclasses.Singleton import Singleton

logger = Logger(__name__)


class StorageOptionManager(metaclass=Singleton):

    SORT_FIELD_NONE: int = -1

    SORT_FIELD_DEFAULT: int = 0

    SORT_FIELD_NAME: int = 1

    SORT_FIELD_WEIGHT: int = 2

    SORT_FIELD_QUANTITY: int = 3

    SORT_FIELD_LOT_WEIGHT: int = 4

    SORT_FIELD_AVERAGEPRICE: int = 5

    SORT_FIELD_LOT_AVERAGEPRICE: int = 6

    SORT_FIELD_LEVEL: int = 7

    SORT_FIELD_ITEM_TYPE: int = 8

    MAX_SORT_FIELDS: int = 2

    _inventory: "Inventory"

    _categoryFilter: int = -1

    _bankCategoryFilter: int = -1

    _filterType: int = -1

    _bankFilterType: int = -1

    _sortFields: list

    _sortRevert: bool

    _sortBankFields: list

    _sortBankRevert: bool

    _newSort: bool

    _associatedRunesActive: bool = False

    def __init__(self):
        self._sortFields = [-1]
        self._sortBankFields = [-1]
        super().__init__()

    @property
    def category(self) -> int:
        return self._categoryFilter

    @category.setter
    def category(self, cat: int) -> None:
        self._categoryFilter = cat
        self.updateStorageView()

    @property
    def bankCategory(self) -> int:
        return self._bankCategoryFilter

    @bankCategory.setter
    def bankCategory(self, cat: int) -> None:
        self._bankCategoryFilter = cat
        self.updateBankStorageView()

    @property
    def filter(self) -> int:
        return self._filterType

    @filter.setter
    def filter(self, filterType: int) -> None:
        self._filterType = filterType
        if self._filterType != -1:
            if self.category == ItemCategoryEnum.ECAFLIP_CARD_CATEGORY:
                inventorymgr.InventoryManager().inventory.refillView(
                    "storageMinouki", "storageMinoukiFiltered"
                )
            else:
                inventorymgr.InventoryManager().inventory.refillView(
                    "storage", "storageFiltered"
                )
        self.updateStorageView()

    def hasFilter(self) -> bool:
        return self._filterType != -1

    @property
    def bankFilter(self) -> int:
        return self._bankFilterType

    @bankFilter.setter
    def bankFilter(self, bankFilterType: int) -> None:
        self._bankFilterType = bankFilterType
        if self._bankFilterType != -1:
            if self.bankCategory == ItemCategoryEnum.ECAFLIP_CARD_CATEGORY:
                inventorymgr.InventoryManager().bankInventory.refillView(
                    "bankMinouki", "bankMinoukiFiltered"
                )
            else:
                inventorymgr.InventoryManager().bankInventory.refillView(
                    "bank", "bankFiltered"
                )
        self.updateBankStorageView()

    def hasBankFilter(self) -> bool:
        return self._bankFilterType != -1

    @property
    def newSort(self) -> bool:
        return self._newSort

    @property
    def sortFields(self) -> list:
        return self._sortFields

    @property
    def sortField(self):
        raise RuntimeError("This property has no getter!")

    @sortField.setter
    def sortField(self, fieldName: int) -> None:
        if fieldName not in self._sortFields:
            if fieldName != self.SORT_FIELD_NONE and len(self._sortFields) > 0:
                self._newSort = False
            if len(self._sortFields) <= self.MAX_SORT_FIELDS - 1:
                self._sortFields.append(fieldName)
            else:
                self._sortFields[self.MAX_SORT_FIELDS - 1] = fieldName
        else:
            self._newSort = True
        self.currentStorageView.updateView()
        self._newSort = False

    def hasSort(self) -> bool:
        return self._sortFields[0] != self.SORT_FIELD_NONE

    @property
    def sortRevert(self) -> bool:
        return self._sortRevert

    @sortRevert.setter
    def sortRevert(self, revert: bool) -> None:
        self._sortRevert = revert

    def resetSort(self) -> None:
        self._newSort = True
        self._sortFields = list()

    @property
    def sortBankField(self):
        raise RuntimeError("This property has no getter!")

    @sortBankField.setter
    def sortBankField(self, fieldName: int) -> None:
        currentItems: list[ItemWrapper] = None
        itemsDisplayed: list[ItemWrapper] = None
        iw: ItemWrapper = None
        if fieldName not in self._sortBankFields:
            if fieldName != self.SORT_FIELD_NONE and len(self._sortBankFields) > 0:
                self._newSort = False
            if len(self._sortBankFields) <= self.MAX_SORT_FIELDS - 1:
                self._sortBankFields.append(fieldName)
            else:
                self._sortBankFields[self.MAX_SORT_FIELDS - 1] = fieldName
        else:
            self._newSort = True
        if not self._associatedRunesActive:
            self.currentBankView.updateView()
            if self.hasBankFilter():
                currentItems = self.currentBankView.content
                itemsDisplayed = list[ItemWrapper]()
                for iw in currentItems:
                    if iw.typeId == self.bankFilter:
                        itemsDisplayed.append(iw.clone())
        else:
            inventorymgr.InventoryManager().bankInventory.getView(
                "bankAssociatedRunes"
            ).updateView()
        self._newSort = False

    @property
    def sortBankFields(self) -> list:
        return self._sortBankFields

    def resetBankSort(self) -> None:
        self._newSort = True
        self._sortBankFields = list()

    @property
    def sortBankRevert(self) -> bool:

        return self._sortBankRevert

    @sortBankRevert.setter
    def sortBankRevert(self, revert: bool) -> None:
        self._sortBankRevert = revert

    @property
    def currentStorageView(self) -> IStorageView:
        view = None
        view = self.inventory.getView("storageBidHouseFilter")
        if view:
            return view
        view = self.inventory.getView("storageSmithMagicFilter")
        if view:
            return view
        view = self.inventory.getView("storageCraftFilter")
        if view:
            return view
        view = self.inventory.getView("forgettableSpellsFilter")
        if view:
            return view
        return self.getStorageViewOrFilter()

    def getStorageViewOrFilter(self) -> IStorageView:
        if self.hasFilter():
            return self.inventory.getView(
                "storageFiltered"
                if self.category != ItemCategoryEnum.ECAFLIP_CARD_CATEGORY
                else "storageMinoukiFiltered"
            )
        return self.getStorageView(self.category)

    @property
    def currentBankView(self) -> IStorageView:
        if (
            self.hasBankFilter()
            and self.bankCategory == ItemCategoryEnum.ECAFLIP_CARD_CATEGORY
        ):
            return inventorymgr.InventoryManager().bankInventory.getView(
                "bankMinoukiFiltered"
            )
        return self.getBankView(self.bankCategory)

    def enableBidHouseFilter(self, allowedTypes: list[int], maxItemLevel: int) -> None:
        self.disableBidHouseFilter()
        name: str = self.currentStorageView.name
        self.inventory.addView(
            StorageBidHouseFilterView(
                self.inventory.hookLock,
                self.currentStorageView,
                allowedTypes,
                maxItemLevel,
            )
        )
        inventorymgr.InventoryManager().inventory.refillView(
            name, "storageBidHouseFilter"
        )

    def disableBidHouseFilter(self) -> None:
        if self.inventory.getView("storageBidHouseFilter"):
            self.inventory.removeView("storageBidHouseFilter")

    def getIsBidHouseFilterEnabled(self) -> bool:
        return self.inventory.getView("storageBidHouseFilter") != None

    def enableSmithMagicFilter(self, skill: Skill) -> None:
        from com.ankamagames.dofus.logic.game.common.frames.CraftFrame import CraftFrame

        craftFrame: CraftFrame = None
        self.disableSmithMagicFilter()
        if not skill:
            craftFrame = Kernel.getWorker().getFrame(CraftFrame)
            if not craftFrame:
                logger.error(
                    "Activation des filtres de forgemagie alors que la craftFrame n'est pas active"
                )
                return
            skill = Skill.getSkillById(craftFrame.skillId)
        name: str = self.currentStorageView.name
        self.inventory.addView(
            StorageSmithMagicFilterView(
                self.inventory.hookLock, self.currentStorageView, skill
            )
        )
        inventorymgr.InventoryManager().inventory.refillView(
            name, "storageSmithMagicFilter"
        )

    def disableSmithMagicFilter(self) -> None:
        if self.inventory.getView("storageSmithMagicFilter"):
            self.inventory.removeView("storageSmithMagicFilter")

    def enableCraftFilter(self, skill: Skill, jobLevel: int) -> None:
        craftFrame: CraftFrame = None
        self.disableCraftFilter()
        if not skill:
            craftFrame = Kernel.getWorker().getFrame(CraftFrame)
            if not craftFrame:
                logger.error(
                    "Activation des filtres de forgemagie alors que la craftFrame n'est pas active"
                )
                return
            skill = Skill.getSkillById(craftFrame.skillId)
        name: str = self.currentStorageView.name
        self.inventory.addView(
            StorageCraftFilterView(
                self.inventory.hookLock, self.currentStorageView, skill.id, jobLevel
            )
        )
        inventorymgr.InventoryManager().inventory.refillView(name, "storageCraftFilter")

    def disableCraftFilter(self) -> None:
        if self.inventory.getView("storageCraftFilter"):
            self.inventory.removeView("storageCraftFilter")

    def getIsSmithMagicFilterEnabled(self) -> bool:
        return self.inventory.getView("storageSmithMagicFilter") != None

    def getIsCraftFilterEnabled(self) -> bool:
        return self.inventory.getView("storageCraftFilter") != None

    def getStorageView(self, category: int) -> IStorageView:
        if category == ItemCategoryEnum.EQUIPMENT_CATEGORY:
            return self.inventory.getView("storageEquipment")
        if category == ItemCategoryEnum.CONSUMABLES_CATEGORY:
            return self.inventory.getView("storageConsumables")
        if category == ItemCategoryEnum.RESOURCES_CATEGORY:
            return self.inventory.getView("storageResources")
        if category == ItemCategoryEnum.COSMETICS_CATEGORY:
            return self.inventory.getView("storageCosmetics")
        if category == ItemCategoryEnum.QUEST_CATEGORY:
            return self.inventory.getView("storageQuest")
        if category == ItemCategoryEnum.ECAFLIP_CARD_CATEGORY:
            return self.inventory.getView("storageMinouki")
        if category == ItemCategoryEnum.ALL_CATEGORY:
            return self.inventory.getView("storage")

    def getBankView(self, category: int) -> IStorageView:
        if category == ItemCategoryEnum.EQUIPMENT_CATEGORY:
            return inventorymgr.InventoryManager().bankInventory.getView(
                "bankEquipement"
            )
        if category == ItemCategoryEnum.CONSUMABLES_CATEGORY:
            return inventorymgr.InventoryManager().bankInventory.getView(
                "bankConsumables"
            )
        if category == ItemCategoryEnum.RESOURCES_CATEGORY:
            return inventorymgr.InventoryManager().bankInventory.getView(
                "bankRessources"
            )
        if category == ItemCategoryEnum.COSMETICS_CATEGORY:
            return inventorymgr.InventoryManager().bankInventory.getView(
                "bankCosmetics"
            )
        if category == ItemCategoryEnum.QUEST_CATEGORY:
            return inventorymgr.InventoryManager().bankInventory.getView("bankQuest")
        if category == ItemCategoryEnum.ECAFLIP_CARD_CATEGORY:
            return inventorymgr.InventoryManager().bankInventory.getView("bankMinouki")
        if category == ItemCategoryEnum.ALL_CATEGORY:
            return inventorymgr.InventoryManager().bankInventory.getView("bank")

    def getCategoryTypes(self, category: int) -> dict:
        return self.getStorageView(category).types

    def getBankCategoryTypes(self, category: int) -> dict:
        return self.getBankView(category).types

    def updateStorageView(self) -> None:
        self._newSort = False
        self.refreshViews()
        self.currentStorageView.updateView()

    def updateBankStorageView(self) -> None:
        self._newSort = False
        self.currentBankView.updateView()

    @property
    def inventory(self) -> "Inventory":
        if not self._inventory:
            self._inventory = inventorymgr.InventoryManager().inventory
        return self._inventory

    def refreshViews(self) -> None:
        parentView: IStorageView = self.getStorageViewOrFilter()
        if self.getIsBidHouseFilterEnabled():
            bidHouseFilterView = self.inventory.getView("storageBidHouseFilter")
            bidHouseFilterView.parent = parentView
            self.refreshView("storageBidHouseFilter")
        if self.getIsSmithMagicFilterEnabled():
            smithMagicFilterView = self.inventory.getView("storageSmithMagicFilter")
            smithMagicFilterView.parent = parentView
            self.refreshView("storageSmithMagicFilter")
        if self.getIsCraftFilterEnabled():
            craftFilterView = self.inventory.getView("storageCraftFilter")
            craftFilterView.parent = parentView
            self.refreshView("storageCraftFilter")
        if self.getIsForgettableSpellsFilterEnabled():
            forgettableSpellsFilterView = self.inventory.getView(
                "forgettableSpellsFilter"
            )
            forgettableSpellsFilterView.parent = parentView
            self.refreshView("forgettableSpellsFilter")

    def refreshView(self, viewName: str) -> None:
        view: IInventoryView = self.inventory.getView(viewName)
        self.inventory.removeView(viewName)
        name: str = self.currentStorageView.name
        self.inventory.addView(view)
        inventorymgr.InventoryManager().inventory.refillView(name, viewName)

    def getIsForgettableSpellsFilterEnabled(self) -> bool:
        return self.inventory.getView("forgettableSpellsFilter") is not None

    def enableForgettableSpellsFilter(
        self, allowedTypes: list[int], isHideLearnedSpells: bool
    ) -> None:
        self.disableBidHouseFilter()
        self.inventory.addView(
            ForgettableSpellsFilterView(
                self.inventory.hookLock,
                self.currentStorageView,
                allowedTypes,
                isHideLearnedSpells,
            )
        )
        inventorymgr.InventoryManager().inventory.refillView(
            "storageResources", "forgettableSpellsFilter"
        )

    def disableForgettableSpellsFilter(self) -> None:
        if self.inventory.getView("forgettableSpellsFilter"):
            self.inventory.removeView("forgettableSpellsFilter")

    def enableBankAssociatedRunesFilter(self, item: ItemWrapper) -> None:
        inventorymgr.InventoryManager().bankInventory.addView(
            BankAssociatedRunesView(
                inventorymgr.InventoryManager().bankInventory.hookLock, item
            )
        )
        inventorymgr.InventoryManager().bankInventory.refillView(
            "bankRessources", "bankAssociatedRunes"
        )
        self._associatedRunesActive = True

    def disableBankAssociatedRunesFilter(self) -> None:
        if inventorymgr.InventoryManager().bankInventory.getView("bankAssociatedRunes"):
            inventorymgr.InventoryManager().bankInventory.removeView(
                "bankAssociatedRunes"
            )
        self._associatedRunesActive = False
