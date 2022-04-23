from com.ankamagames.dofus.datacenter.items.criterion.ItemCriterion import ItemCriterion
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class GiftItemCriterion(ItemCriterion, IDataCenter):

    _aliGiftId: int

    _aliGiftLevel: int = -1

    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)
        arrayParams: list = str(self._criterionValueText).split(",")
        if arrayParams and len(arrayParams) > 0:
            if len(arrayParams) <= 2:
                self._aliGiftId = int(arrayParams[0])
                self._aliGiftLevel = int(arrayParams[1])
        else:
            self._aliGiftId = int(self._criterionValue)
            self._aliGiftLevel = -1

    @property
    def isRespected(self) -> bool:
        rgI: int = 0
        rank: int = Kernel().getWorker().getFrame(AlignmentFrame)
        rankGift: AlignmentRankJntGift = (
            AlignmentRankJntGift.getAlignmentRankJntGiftById(rank)
        )
        if rankGift and rankGift.gifts:
            for rgI in range(len(rankGift.gifts)):
                if rankGift.gifts[rgI] == self._aliGiftId:
                    if self._aliGiftLevel != 0:
                        if rankGift.levels[rgI] > self._aliGiftLevel:
                            return True
                        return False
                    return True
        return False

    @property
    def text(self) -> str:
        criterionInfo: list = None
        if _operator.text == ">":
            criterionInfo = _criterionValueText.split(",")
            return I18n.getUiText(
                "ui.pvp.giftRequired",
                [
                    AlignmentGift.getAlignmentGiftById(self._aliGiftId).name
                    + " > "
                    + self._aliGiftLevel
                ],
            )
        return I18n.getUiText(
            "ui.pvp.giftRequired",
            [AlignmentGift.getAlignmentGiftById(self._aliGiftId).name],
        )

    def clone(self) -> IItemCriterion:
        return GiftItemCriterion(self.basicText)
