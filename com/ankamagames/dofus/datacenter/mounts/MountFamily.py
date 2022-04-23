from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class MountFamily(IDataCenter):

    MODULE: str = "MountFamily"

    id: int

    nameId: int

    headUri: str

    _name: str

    def __init__(self):
        super().__init__()

    @classmethod
    def getMountFamilyById(cls, id: int) -> "MountFamily":
        return GameData.getObject(cls.MODULE, id)

    @classmethod
    def getMountFamilies(cls) -> list["MountFamily"]:
        return GameData.getobjects(cls.MODULE)

    idAccessors: IdAccessors = IdAccessors(getMountFamilyById, getMountFamilies)

    @property
    def name(self) -> str:
        if not self._name:
            self._name = I18n.getText(self.nameId)
        return self._name
