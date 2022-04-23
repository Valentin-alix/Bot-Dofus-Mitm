from sys import argv
from com.ankamagames.dofus.misc.utils.AbstractAction import AbstractAction
from com.ankamagames.jerakine.handlers.messages.Action import Action


class GameContextQuitAction(AbstractAction, Action):
    def __init__(self, params: list = None):
        super().__init__(params)

    @classmethod
    def create(cls) -> "GameContextQuitAction":
        return GameContextQuitAction(argv)
