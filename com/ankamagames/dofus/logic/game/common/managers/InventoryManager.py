from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
from com.ankamagames.dofus.logic.game.common.misc.Inventory import Inventory
from com.ankamagames.dofus.logic.game.common.misc.PlayerInventory import PlayerInventory
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.BankConsumablesView import (
    BankConsumablesView,
)
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.BankCosmeticsView import (
    BankCosmeticsView,
)
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.BankEquipementView import (
    BankEquipementView,
)
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.BankFilteredView import (
    BankFilteredView,
)
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.BankMinoukiFilteredView import (
    BankMinoukiFilteredView,
)
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.BankMinoukiView import (
    BankMinoukiView,
)
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.BankQuestView import (
    BankQuestView,
)
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.BankRessourcesView import (
    BankRessourcesView,
)
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.BankView import BankView
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.CertificateView import (
    CertificateView,
)
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.EquipmentView import (
    EquipmentView,
)
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.RealView import RealView
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.RoleplayBuffView import (
    RoleplayBuffView,
)
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.StorageConsumablesView import (
    StorageConsumablesView,
)
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.StorageCosmeticsView import (
    StorageCosmeticsView,
)
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.StorageEquipmentView import (
    StorageEquipmentView,
)
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.StorageFilteredView import (
    StorageFilteredView,
)
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.StorageMinoukiFilteredView import (
    StorageMinoukiFilteredView,
)
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.StorageMinoukiView import (
    StorageMinoukiView,
)
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.StorageQuestCategory import (
    StorageQuestCategory,
)
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.StorageResourcesView import (
    StorageResourcesView,
)
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.StorageView import (
    StorageView,
)
from com.ankamagames.dofus.network.ProtocolConstantsEnum import ProtocolConstantsEnum
from com.ankamagames.dofus.network.enums.CharacterInventoryPositionEnum import (
    CharacterInventoryPositionEnum,
)
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.metaclasses.Singleton import Singleton

logger = Logger(__name__)


class InventoryManager(metaclass=Singleton):

    _watchSelf: "InventoryManager"

    _inventory: Inventory

    _bankInventory: Inventory

    _shortcutBarSpells: list

    _shortcutBarItems: list

    _builds: list

    _currentBuildId: int = -1

    _maxBuildCount: int

    _presetsItemPositionsOrder: list

    def __init__(self):
        self._presetsItemPositionsOrder = [
            CharacterInventoryPositionEnum.ACCESSORY_POSITION_HAT,
            CharacterInventoryPositionEnum.ACCESSORY_POSITION_CAPE,
            CharacterInventoryPositionEnum.ACCESSORY_POSITION_BELT,
            CharacterInventoryPositionEnum.ACCESSORY_POSITION_BOOTS,
            CharacterInventoryPositionEnum.ACCESSORY_POSITION_AMULET,
            CharacterInventoryPositionEnum.INVENTORY_POSITION_RING_LEFT,
            CharacterInventoryPositionEnum.INVENTORY_POSITION_RING_RIGHT,
            CharacterInventoryPositionEnum.INVENTORY_POSITION_COSTUME,
            CharacterInventoryPositionEnum.ACCESSORY_POSITION_WEAPON,
            CharacterInventoryPositionEnum.ACCESSORY_POSITION_SHIELD,
            CharacterInventoryPositionEnum.INVENTORY_POSITION_ENTITY,
            CharacterInventoryPositionEnum.ACCESSORY_POSITION_PETS,
            CharacterInventoryPositionEnum.INVENTORY_POSITION_DOFUS_1,
            CharacterInventoryPositionEnum.INVENTORY_POSITION_DOFUS_2,
            CharacterInventoryPositionEnum.INVENTORY_POSITION_DOFUS_3,
            CharacterInventoryPositionEnum.INVENTORY_POSITION_DOFUS_4,
            CharacterInventoryPositionEnum.INVENTORY_POSITION_DOFUS_5,
            CharacterInventoryPositionEnum.INVENTORY_POSITION_DOFUS_6,
        ]
        super().__init__()
        self._maxBuildCount = ProtocolConstantsEnum.MAX_PRESET_COUNT
        self._inventory = PlayerInventory()
        self._builds = list()
        self._shortcutBarItems = list()
        self._shortcutBarSpells = list()
        self.inventory.addView(RealView(self.inventory.hookLock))
        self.inventory.addView(EquipmentView(self.inventory.hookLock))
        self.inventory.addView(RoleplayBuffView(self.inventory.hookLock))
        self.inventory.addView(CertificateView(self.inventory.hookLock))
        self.inventory.addView(StorageView(self.inventory.hookLock))
        self.inventory.addView(StorageEquipmentView(self.inventory.hookLock))
        self.inventory.addView(StorageConsumablesView(self.inventory.hookLock))
        self.inventory.addView(StorageResourcesView(self.inventory.hookLock))
        self.inventory.addView(StorageCosmeticsView(self.inventory.hookLock))
        self.inventory.addView(StorageMinoukiView(self.inventory.hookLock))
        self.inventory.addView(StorageMinoukiFilteredView(self.inventory.hookLock))
        self.inventory.addView(StorageQuestCategory(self.inventory.hookLock))
        self.inventory.addView(StorageFilteredView(self.inventory.hookLock))

    def getInstance(self) -> "InventoryManager":
        if not _self:
            _self = InventoryManager()
        return _self

    def getWatchInstance(self) -> "InventoryManager":
        if not _watchSelf:
            _watchSelf = InventoryManager()
        return _watchSelf

    def init(self) -> None:
        self._inventory.initialize(list[ItemWrapper]())
        self._builds = list()
        self._shortcutBarItems = list()
        self._shortcutBarSpells = list()

    @property
    def inventory(self) -> Inventory:
        return self._inventory

    @property
    def realInventory(self) -> list[ItemWrapper]:
        return self._inventory.getView("real").content

    @property
    def builds(self) -> list:
        return self._builds

    @builds.setter
    def builds(self, builds: list) -> None:
        self._builds = builds

    @property
    def bankInventory(self) -> Inventory:
        if not self._bankInventory:
            self._bankInventory = Inventory()
            self._bankInventory.addView(BankView(self._bankInventory.hookLock))
            self._bankInventory.addView(
                BankEquipementView(self._bankInventory.hookLock)
            )
            self._bankInventory.addView(
                BankConsumablesView(self._bankInventory.hookLock)
            )
            self._bankInventory.addView(
                BankRessourcesView(self._bankInventory.hookLock)
            )
            self._bankInventory.addView(BankCosmeticsView(self._bankInventory.hookLock))
            self._bankInventory.addView(BankQuestView(self._bankInventory.hookLock))
            self._bankInventory.addView(BankMinoukiView(self._bankInventory.hookLock))
            self._bankInventory.addView(
                BankMinoukiFilteredView(self._bankInventory.hookLock)
            )
            self._bankInventory.addView(BankFilteredView(self._bankInventory.hookLock))
        return self._bankInventory

    @property
    def shortcutBarItems(self) -> list:
        return self._shortcutBarItems

    @shortcutBarItems.setter
    def shortcutBarItems(self, aItems: list) -> None:
        self._shortcutBarItems = aItems

    @property
    def shortcutBarSpells(self) -> list:
        return self._shortcutBarSpells

    @shortcutBarSpells.setter
    def shortcutBarSpells(self, aSpells: list) -> None:
        self._shortcutBarSpells = aSpells

    def getMaxItemsCountForPreset(self) -> int:
        return len(self._presetsItemPositionsOrder)

    def getPositionForPresetItemIndex(self, index: int) -> int:
        return self._presetsItemPositionsOrder[index]

    @property
    def currentBuildId(self) -> int:
        return self._currentBuildId

    @currentBuildId.setter
    def currentBuildId(self, value: int) -> None:
        self._currentBuildId = value
