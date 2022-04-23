class SoulStoneItemCriterion(ItemCriterion, IDataCenter):

    ID_SOUL_STONE: list = [
        DataEnum.ITEM_GID_SOULSTONE,
        DataEnum.ITEM_GID_SOULSTONE_MINIBOSS,
        DataEnum.ITEM_GID_SOULSTONE_BOSS,
    ]

    _quantityMonster: int = 1

    _monsterId: int

    _monsterName: str

    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)
        arrayParams: list = str(_criterionValueText).split(",")
        if arrayParams and len(arrayParams) > 0:
            if len(arrayParams) <= 2:
                self._monsterId = int(arrayParams[0])
                self._quantityMonster = int(arrayParams[1])
        else:
            self._monsterId = int(_criterionValue)
        self._monsterName = Monster.getMonsterById(self._monsterId).name

    @property
    def isRespected(self) -> bool:
        iw: ItemWrapper = None
        soulStoneId: int = 0
        for iw in InventoryManager().realInventory:
            for soulStoneId in ID_SOUL_STONE:
                if iw.objectGID == soulStoneId:
                    return True
        return False

    @property
    def text(self) -> str:
        return I18n.getUiText(
            "ui.tooltip.possessSoulStone", [self._quantityMonster, self._monsterName]
        )

    def clone(self) -> IItemCriterion:
        return SoulStoneItemCriterion(self.basicText)
