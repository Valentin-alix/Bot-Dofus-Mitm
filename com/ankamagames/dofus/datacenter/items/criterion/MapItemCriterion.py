class MapItemCriterion(ItemCriterion, IDataCenter):

    _mapId: float

    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)
        if PlayedCharacterManager().currentMap:
            self._mapId = PlayedCharacterManager().currentMap.mapId

    @property
    def text(self) -> str:
        return ""

    def clone(self) -> IItemCriterion:
        return MapItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        self._mapId = PlayedCharacterManager().currentMap.mapId
        return self._mapId
