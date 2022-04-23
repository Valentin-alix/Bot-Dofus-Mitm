from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class RandomDropItem(IDataCenter):

    id: int

    itemId: int

    probability: float

    minQuantity: int

    maxQuantity: int

    _item: ItemWrapper

    def __init__(self):
        super().__init__()

    @property
    def itemWrapper(self) -> ItemWrapper:
        if not self._item:
            self._item = ItemWrapper.create(0, 0, self.itemId, 0, None)
        return self._item
