from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
import com.ankamagames.dofus.logic.game.common.managers.InventoryManager as inventorymgr
from com.ankamagames.dofus.network.enums.CharacterInventoryPositionEnum import (
    CharacterInventoryPositionEnum,
)
from com.ankamagames.dofus.network.types.game.presets.ItemForPreset import ItemForPreset
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter
from com.ankamagames.jerakine.interfaces.ISlotDataHolder import ISlotDataHolder
from com.ankamagames.jerakine.logger.Logger import Logger

logger = Logger(__name__)


class PresetWrapper(ItemWrapper, IDataCenter):

    gfxId: int

    _objects: list

    mount: bool

    _uri: str

    _pngMode: bool

    def __init__(self):
        super().__init__()

    def create(
        self, id: int, gfxId: int, objects: list[ItemForPreset], mount: bool = False
    ) -> "PresetWrapper":

        mountFakeItemWrapper: MountWrapper = None
        itemsCount: int = inventorymgr.InventoryManager().getMaxItemsCountForPreset()
        presetWrapper: PresetWrapper = PresetWrapper()
        presetWrapper.id = id
        presetWrapper.gfxId = gfxId
        presetWrapper.objects = list(itemsCount)
        presetWrapper.mount = mount
        for i in range(itemsCount):
            pos = inventorymgr.InventoryManager().getPositionForPresetItemIndex(i)
            objExists = False
            for item in objects:
                if item.position == pos:
                    if item.objUid:
                        presetWrapper.objects[i] = inventorymgr.InventoryManager().inventory.getItem(
                            item.objUid
                        )
                    else:
                        presetWrapper.objects[i] = ItemWrapper.create(
                            0, 0, item.objGid, 1, None, False
                        )
                        presetWrapper.objects[i].active = False
                    objExists = True
            if (
                pos == CharacterInventoryPositionEnum.ACCESSORY_POSITION_PETS
                and not objExists
                and mount
            ):
                mountFakeItemWrapper = MountWrapper.create()
                presetWrapper.objects[i] = mountFakeItemWrapper
                presetWrapper.objects[i].backGroundIconUri = None
                objExists = True
        return presetWrapper

    def getSlotNameByPositionId(self, i: int) -> str:
        pos: int = inventorymgr.InventoryManager().getPositionForPresetItemIndex(i)
        if pos == CharacterInventoryPositionEnum.ACCESSORY_POSITION_AMULET:
            return "collar"
        if pos == CharacterInventoryPositionEnum.ACCESSORY_POSITION_WEAPON:
            return "weapon"
        if (
            pos == CharacterInventoryPositionEnum.INVENTORY_POSITION_RING_LEFT
            or pos == CharacterInventoryPositionEnum.INVENTORY_POSITION_RING_RIGHT
        ):
            return "ring"
        if pos == CharacterInventoryPositionEnum.ACCESSORY_POSITION_BELT:
            return "belt"
        if pos == CharacterInventoryPositionEnum.ACCESSORY_POSITION_BOOTS:
            return "shoe"
        if pos == CharacterInventoryPositionEnum.ACCESSORY_POSITION_HAT:
            return "helmet"
        if pos == CharacterInventoryPositionEnum.ACCESSORY_POSITION_CAPE:
            return "cape"
        if pos == CharacterInventoryPositionEnum.ACCESSORY_POSITION_PETS:
            return "pet"
        if pos in [
            CharacterInventoryPositionEnum.INVENTORY_POSITION_DOFUS_1,
            CharacterInventoryPositionEnum.INVENTORY_POSITION_DOFUS_2,
            CharacterInventoryPositionEnum.INVENTORY_POSITION_DOFUS_3,
            CharacterInventoryPositionEnum.INVENTORY_POSITION_DOFUS_4,
            CharacterInventoryPositionEnum.INVENTORY_POSITION_DOFUS_5,
            CharacterInventoryPositionEnum.INVENTORY_POSITION_DOFUS_6,
        ]:
            return "dofus"
        if pos == CharacterInventoryPositionEnum.ACCESSORY_POSITION_SHIELD:
            return "shield"
        if pos == CharacterInventoryPositionEnum.INVENTORY_POSITION_ENTITY:
            return "companon"
        if pos == CharacterInventoryPositionEnum.INVENTORY_POSITION_COSTUME:
            return "costume"
        else:
            return "companon"

    @property
    def objects(self) -> list:
        return self._objects

    @objects.setter
    def objects(self, a: list) -> None:
        self._objects = a

    @property
    def info1(self) -> str:
        return None

    @property
    def timer(self) -> int:
        return 0

    @property
    def active(self) -> bool:
        return True

    def updateObject(self, object: ItemForPreset) -> None:
        pass

    def addHolder(self, h: ISlotDataHolder) -> None:
        pass

    def removeHolder(self, h: ISlotDataHolder) -> None:
        pass
