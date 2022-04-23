from sys import argv
from com.ankamagames.dofus.misc.utils.AbstractAction import AbstractAction
from com.ankamagames.jerakine.handlers.messages.Action import Action


class PopupWarningCloseRequestAction(AbstractAction, Action):
    def __init__(self, params: list = None):
        super().__init__(params)

    def create(self) -> "PopupWarningCloseRequestAction":
        return PopupWarningCloseRequestAction(argv)
