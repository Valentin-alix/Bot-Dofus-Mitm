from sys import argv
from com.ankamagames.dofus.misc.utils.AbstractAction import AbstractAction
from com.ankamagames.jerakine.handlers.messages.Action import Action


class PlayerFightRequestAction(AbstractAction, Action):

    targetedPlayerId: float

    cellId: int

    friendly: bool

    launch: bool

    ava: bool

    def __init__(self, params: list = None):
        super().__init__(params)

    def create(
        self,
        targetedPlayerId: float,
        ava: bool,
        friendly: bool = True,
        launch: bool = False,
        cellId: int = -1,
    ) -> "PlayerFightRequestAction":
        o: PlayerFightRequestAction = PlayerFightRequestAction(argv)
        o.ava = ava
        o.friendly = friendly
        o.cellId = cellId
        o.targetedPlayerId = targetedPlayerId
        o.launch = launch
        return o
