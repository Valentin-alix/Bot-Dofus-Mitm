from com.ankamagames.dofus.misc.utils.AbstractAction import AbstractAction
from com.ankamagames.jerakine.handlers.messages.Action import Action


class UpdateSpellModifierAction(AbstractAction, Action):
    def __init__(self, entityId: float, spellId: float, statId: float):
        super().__init__(None)
        self._entityId = entityId
        self._spellId = spellId
        self._statId = statId

    def create(
        cls, entityId: float, spellId: float, statId: float
    ) -> "UpdateSpellModifierAction":
        return cls(entityId, spellId, statId)

    @property
    def entityId(self) -> float:
        return self._entityId

    @property
    def spellId(self) -> float:
        return self._spellId

    @property
    def statId(self) -> float:
        return self._statId
