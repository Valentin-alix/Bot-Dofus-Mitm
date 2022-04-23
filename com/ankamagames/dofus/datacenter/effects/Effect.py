from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class Effect(IDataCenter):

    MODULE: str = "Effects"

    id: int

    descriptionId: int

    iconId: int

    characteristic: int

    category: int

    operator: str

    showInTooltip: bool

    useDice: bool

    forceMinMax: bool

    boost: bool

    active: bool

    oppositeId: int

    theoreticalDescriptionId: int

    theoreticalPattern: int

    showInSet: bool

    bonusType: int

    useInFight: bool

    effectPriority: int

    effectPowerRate: float

    elementId: int

    _description: str

    _theoricDescription: str

    def __init__(self):
        super().__init__()

    def getEffectById(id: int) -> "Effect":
        return GameData.getObject(Effect.MODULE, id)

    idAccessors: IdAccessors = IdAccessors(getEffectById, None)

    @property
    def description(self) -> str:
        if not self._description:
            self._description = I18n.getText(self.descriptionId)
        return self._description

    @property
    def theoreticalDescription(self) -> str:
        if not self._theoricDescription:
            self._theoricDescription = I18n.getText(self.theoreticalDescriptionId)
        return self._theoricDescription
