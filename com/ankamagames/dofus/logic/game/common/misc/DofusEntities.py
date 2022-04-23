from com.ankamagames.atouin.managers.EntitiesManager import EntitiesManager
from com.ankamagames.dofus.logic.game.misc.IEntityLocalizer import IEntityLocalizer
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.entities.interfaces.IEntity import IEntity

logger = Logger(__name__)


class DofusEntities:

    LOCALIZER_DEBUG: bool = True
    _localizers: list[IEntityLocalizer] = list[IEntityLocalizer]()

    @classmethod
    def getEntity(cls, entityId: float) -> IEntity:
        localizer: IEntityLocalizer = None
        foundEntity: IEntity = None
        for localizer in cls._localizers:
            foundEntity = localizer.getEntity(entityId)
            if foundEntity:
                return foundEntity
        return EntitiesManager().getEntity(entityId)

    @classmethod
    def registerLocalizer(cls, localizer: IEntityLocalizer) -> None:
        currentLocalizer: IEntityLocalizer = None
        clazz: str = localizer.__class__.__name__
        currentClazz: str = None
        for currentLocalizer in cls._localizers:
            currentClazz = currentLocalizer.__class__.__name__
            if currentClazz == clazz:
                raise Exception(
                    "There's more than one "
                    + currentClazz
                    + " localizer added to DofusEntites. Nope, that won't work."
                )
        cls._localizers.append(localizer)

    @classmethod
    def reset(cls) -> None:
        localizer: IEntityLocalizer = None
        for i in range(0, len(cls._localizers), 1):
            localizer = cls._localizers[i]
            localizer.unregistered()
        cls._localizers = list[IEntityLocalizer]()
