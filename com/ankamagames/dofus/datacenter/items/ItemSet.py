from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter
from com.ankamagames.dofus.datacenter.effects.EffectInstance import EffectInstance


class ItemSet(IDataCenter):

    MODULE: str = "ItemSets"

    id: int

    items: list[int]

    nameId: int

    effects: list[list[EffectInstance]]

    bonusIsSecret: bool

    _name: str

    def __init__(self):
        super().__init__()

    @staticmethod
    def getItemSetById(id: int) -> "ItemSet":
        return GameData.getObject(ItemSet.MODULE, id)

    def getItemSets(self) -> list:
        return GameData.getObjects(ItemSet.MODULE)

    @property
    def name(self) -> str:
        if not self._name:
            self._name = I18n.getText(self.nameId)
        return self._name
