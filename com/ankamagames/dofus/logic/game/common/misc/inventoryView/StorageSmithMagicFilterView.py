from com.ankamagames.dofus.datacenter.jobs.Skill import Skill
from com.ankamagames.dofus.internalDatacenter.DataEnum import DataEnum
from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
from com.ankamagames.dofus.logic.game.common.misc.IStorageView import IStorageView
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.StorageGenericView import (
    StorageGenericView,
)


class StorageSmithMagicFilterView(StorageGenericView):

    _skill: Skill

    _parent: IStorageView

    _listeningItemTypes: list

    def __init__(self, parentView: IStorageView, skill: Skill):
        self._listeningItemTypes = [
            DataEnum.ITEM_TYPE_SMITHMAGIC_RUNE,
            DataEnum.ITEM_TYPE_SMITHMAGIC_POTION,
            DataEnum.ITEM_TYPE_SMITHMAGIC_ORB,
            DataEnum.ITEM_TYPE_SMITHMAGIC_TRANSCENDANCE_RUNE,
            DataEnum.ITEM_TYPE_SMITHMAGIC_CORRUPTION_RUNE,
        ]
        super().__init__()
        self._skill = skill
        self._parent = parentView

    @property
    def name(self) -> str:
        return "storageSmithMagicFilter"

    def isListening(self, item: ItemWrapper) -> bool:
        return (
            self._parent.isListening(item)
            and super().isListening(item)
            and (
                self._skill.modifiableItemTypeIds.find(item.typeId) != -1
                or self._listeningItemTypes.find(item.typeId) != -1
            )
            or item.objectGID == DataEnum.ITEM_GID_SIGNATURE_RUNE
        )

    def updateView(self) -> None:
        super().updateView()

    @property
    def parent(self) -> IStorageView:
        return self._parent

    @parent.setter
    def parent(self, view: IStorageView) -> None:
        self._parent = view
