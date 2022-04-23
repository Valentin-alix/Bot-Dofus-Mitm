from sys import argv
from com.ankamagames.dofus.misc.utils.AbstractAction import AbstractAction
from com.ankamagames.jerakine.handlers.messages.Action import Action


class CharacterReplayRequestAction(AbstractAction, Action):

    characterId: float

    def __init__(self, params: list = None):
        super().__init__(params)

    def create(self, characterId: float) -> "CharacterReplayRequestAction":
        a: CharacterReplayRequestAction = CharacterReplayRequestAction(argv)
        a.characterId = characterId
        return a
