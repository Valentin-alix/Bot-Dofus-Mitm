from sys import argv
from com.ankamagames.dofus.misc.utils.AbstractAction import AbstractAction
from com.ankamagames.jerakine.handlers.messages.Action import Action


class GameFightPlacementSwapPositionsRequestAction(AbstractAction, Action):

    cellId: int

    requestedId: float

    def __init__(self, params: list = None):
        super().__init__(params)

    @classmethod
    def create(
        cls, pCellId: int, pRequestedId: float
    ) -> "GameFightPlacementSwapPositionsRequestAction":
        action: GameFightPlacementSwapPositionsRequestAction = (
            GameFightPlacementSwapPositionsRequestAction(argv)
        )
        action.cellId = pCellId
        action.requestedId = pRequestedId
        return action
