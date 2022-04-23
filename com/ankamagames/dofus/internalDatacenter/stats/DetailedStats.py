from com.ankamagames.dofus.internalDatacenter.stats.Stat import Stat


class DetailedStat(Stat):
    _baseValue: float = 0
    _additionalValue: float = 0
    _objectsAndMountBonusValue: float = 0
    _alignGiftBonusValue: float = 0
    _contextModifValue: float = 0

    def __init__(
        self,
        id: float,
        baseValue: float,
        additionalValue: float,
        objectsAndMountBonusValue: float,
        alignGiftBonusValue: float,
        contextModifValue: float,
    ):
        self._baseValue = baseValue
        self._additionalValue = additionalValue
        self._objectsAndMountBonusValue = objectsAndMountBonusValue
        self._alignGiftBonusValue = alignGiftBonusValue
        self._contextModifValue = contextModifValue
        super(
            id,
            self._baseValue
            + self._additionalValue
            + self._objectsAndMountBonusValue
            + self._alignGiftBonusValue
            + self._contextModifValue,
        )

    @property
    def baseValue(self) -> float:
        return self._baseValue

    @property
    def additionalValue(self) -> float:
        return self._additionalValue

    @property
    def objectsAndMountBonusValue(self) -> float:
        return self._objectsAndMountBonusValue

    @property
    def alignGiftBonusValue(self) -> float:
        return self._alignGiftBonusValue

    @property
    def contextModifValue(self) -> float:
        return self._contextModifValue

    @baseValue.setter
    def baseValue(self, value: float) -> None:
        self._baseValue = value
        self.updateTotal()

    @additionalValue.setter
    def additionalValue(self, value: float) -> None:
        self._additionalValue = value
        self.updateTotal()

    @objectsAndMountBonusValue.setter
    def objectsAndMountBonusValue(self, value: float) -> None:
        self._objectsAndMountBonusValue = value
        self.updateTotal()

    @alignGiftBonusValue.setter
    def alignGiftBonusValue(self, value: float) -> None:
        self._alignGiftBonusValue = value
        self.updateTotal()

    @contextModifValue.setter
    def contextModifValue(self, value: float) -> None:
        self._contextModifValue = value
        self.updateTotal()

    def __str__(self) -> str:
        return self.getFormattedMessage(
            "base: "
            + self._baseValue.__str__()
            + " additional: "
            + self._additionalValue.__str__()
            + " objectsAndMountBonus: "
            + self._objectsAndMountBonusValue.__str__()
            + " alignGiftBonus: "
            + self._alignGiftBonusValue.__str__()
            + " contextModif: "
            + self._contextModifValue.__str__()
            + " total: "
            + self._totalValue.__str__()
        )

    def reset(self) -> None:
        self._baseValue = (
            self._additionalValue
        ) = (
            self._objectsAndMountBonusValue
        ) = self._alignGiftBonusValue = self._contextModifValue = _totalValue = 0

    def updateTotal(self) -> None:
        self._totalValue = (
            self._baseValue
            + self._additionalValue
            + self._objectsAndMountBonusValue
            + self._alignGiftBonusValue
            + self._contextModifValue
        )
