from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class MountBehavior(IDataCenter):

    MODULE: str = "MountBehaviors"

    id: int

    nameId: int

    descriptionId: int

    _name: str

    _description: str

    def __init__(self):
        super().__init__()

    @classmethod
    def getMountBehaviorById(cls, id: int) -> "MountBehavior":
        return GameData.getObject(cls.MODULE, id)

    @classmethod
    def getMountBehaviors(cls) -> list["MountBehavior"]:
        return GameData.getobjects(cls.MODULE)

    idAccessors: IdAccessors = IdAccessors(getMountBehaviorById, getMountBehaviors)

    @property
    def name(self) -> str:
        if not self._name:
            self._name = I18n.getText(self.nameId)
        return self._name

    @property
    def description(self) -> str:
        if not self._description:
            self._description = I18n.getText(self.descriptionId)
        return self._description
