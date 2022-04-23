from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.dofus.logic.game.fight.types.FighterStatus import FighterStatus
from com.ankamagames.jerakine.metaclasses.Singleton import Singleton

logger = Logger(__name__)


class FightersStateManager(metaclass=Singleton):
    def __init__(self) -> None:
        self._entityStates = dict()

    def addStateOnTarget(self, targetId: float, stateId: int, delta: int = 1) -> None:
        if not self._entityStates[targetId]:
            self._entityStates[targetId] = dict()

        if not self._entityStates[targetId][stateId]:
            self._entityStates[targetId][stateId] = delta

        else:
            self._entityStates[targetId][stateId] += delta

    def removeStateOnTarget(
        self, targetId: float, stateId: int, delta: int = 1
    ) -> None:
        if not self._entityStates[targetId]:
            logger.error("Can't find state list for " + targetId + " to remove state")
            return

        if self._entityStates[targetId][stateId]:
            self._entityStates[targetId][stateId] -= delta
            if self._entityStates[targetId][stateId] == 0:
                del self._entityStates[targetId][stateId]

    def hasState(self, targetId: float, stateId: int) -> bool:
        if (
            not self._entityStates[targetId]
            or not self._entityStates[targetId][stateId]
        ):
            return False

        return self._entityStates[targetId][stateId] > 0

    def getStates(self, targetId: float) -> list:
        stateId = None
        states: list = list()
        if not self._entityStates[targetId]:
            return states

        for stateId in self._entityStates[targetId]:
            if self._entityStates[targetId][stateId] > 0:
                states.append(stateId)

        return states

    def getStatus(self, targetId: float) -> FighterStatus:
        from com.ankamagames.dofus.datacenter.spells.SpellState import SpellState

        stateId = None
        fighterstatus: FighterStatus = FighterStatus()
        for stateId in self._entityStates[targetId]:

            state = SpellState.getSpellStateById(stateId)
            if state and self._entityStates[targetId][stateId] > 0:
                if state.preventsSpellCast:
                    fighterstatus.cantUseSpells = True

                if state.preventsFight:
                    fighterstatus.cantUseCloseQuarterAttack = True

                if state.cantDealDamage:
                    fighterstatus.cantDealDamage = True

                if state.invulnerable:
                    fighterstatus.invulnerable = True

                if state.incurable:
                    fighterstatus.incurable = True

                if state.cantBeMoved:
                    fighterstatus.cantBeMoved = True

                if state.cantBeappended:
                    fighterstatus.cantBeappended = True

                if state.cantSwitchPosition:
                    fighterstatus.cantSwitchPosition = True

                if state.invulnerableMelee:
                    fighterstatus.invulnerableMelee = True

                if state.invulnerableRange:
                    fighterstatus.invulnerableRange = True

                if state.cantTackle:
                    fighterstatus.cantTackle = True

                if state.cantBeTackled:
                    fighterstatus.cantBeTackled = True

        return fighterstatus

    def endFight(self) -> None:
        self._entityStates = dict()
