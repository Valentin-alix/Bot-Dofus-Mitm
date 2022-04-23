from sys import argv
from com.ankamagames.dofus.misc.utils.AbstractAction import AbstractAction
from com.ankamagames.jerakine.handlers.messages.Action import Action


class GameFightReadyAction(AbstractAction, Action):

    isReady: bool

    def __init__(self, params: list = None):
        super().__init__(params)

    @classmethod
    def create(cls, isReady: bool) -> "GameFightReadyAction":
        a: GameFightReadyAction = GameFightReadyAction(argv)
        a.isReady = isReady
        return a
