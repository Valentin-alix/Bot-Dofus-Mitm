from sys import argv
from com.ankamagames.dofus.misc.utils.AbstractAction import AbstractAction
from com.ankamagames.jerakine.handlers.messages.Action import Action


class ServerSelectionAction(AbstractAction, Action):

    serverId: int

    def __init__(self, *params):
        super().__init__(*params)

    @classmethod
    def create(cls, serverId: int) -> "ServerSelectionAction":
        a = cls(argv)
        a.serverId = serverId
        return a
