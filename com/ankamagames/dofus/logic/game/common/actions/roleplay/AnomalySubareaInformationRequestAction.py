from sys import argv
from com.ankamagames.dofus.misc.utils.AbstractAction import AbstractAction
from com.ankamagames.jerakine.handlers.messages.Action import Action


class AnomalySubareaInformationRequestAction(AbstractAction, Action):

    uiName: str

    def __init__(self, params: list = None):
        super().__init__(params)

    @classmethod
    def create(cls, uiName: str) -> "AnomalySubareaInformationRequestAction":
        action = cls(argv)
        action.uiName = uiName
        return action
