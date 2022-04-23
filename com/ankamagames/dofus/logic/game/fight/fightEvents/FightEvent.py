from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from com.ankamagames.dofus.logic.game.fight.types.BasicBuff import BasicBuff


class FightEvent:

    FIGHT_EVENT_ID_COUNTER: int = 0

    name: str

    targetId: float

    params: list

    checkParams: int

    firstParamToCheck: int

    castingSpellId: int

    order: int

    buff: "BasicBuff"

    id: int

    def __init__(
        self,
        pName: str,
        pParams: list,
        pTargetId: float,
        pCheckParams: int,
        pCastingSpellId: int,
        pOrder: int = -1,
        pFirstParamToCheck: int = 1,
        pBuff: "BasicBuff" = None,
    ):
        super().__init__()
        self.name = pName
        self.targetId = pTargetId
        self.params = pParams
        self.checkParams = pCheckParams
        self.castingSpellId = pCastingSpellId
        self.order = pOrder
        self.firstParamToCheck = pFirstParamToCheck
        self.buff = pBuff
        self.FIGHT_EVENT_ID_COUNTER += 1
        self.id = FightEvent.FIGHT_EVENT_ID_COUNTER

    def reset(self) -> None:
        FIGHT_EVENT_ID_COUNTER = 0
