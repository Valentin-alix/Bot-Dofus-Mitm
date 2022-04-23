class VeteranReward(IDataCenter):

    MODULE: str = "VeteranRewards"

    id: int

    requiredSubDays: int

    itemGID: int

    itemQuantity: int

    _itemWrapper: ItemWrapper

    def __init__(self):
        super().__init__()

    def getAllVeteranRewards(self) -> list:
        return GameData.getObjects(MODULE)

    @property
    def item(self) -> ItemWrapper:
        if not self._itemWrapper:
            self._itemWrapper = ItemWrapper.create(
                0, 0, self.itemGID, self.itemQuantity, None, False
            )
        return self._itemWrapper
