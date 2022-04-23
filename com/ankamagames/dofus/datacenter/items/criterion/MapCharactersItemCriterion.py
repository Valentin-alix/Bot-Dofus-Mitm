class MapCharactersItemCriterion(ItemCriterion, IDataCenter):

    _mapId: float

    _nbCharacters: int

    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)
        params: list = _criterionValueText.split(",")
        if len(params) == 1:
            self._mapId = PlayedCharacterManager().currentMap.mapId
            self._nbCharacters = int(params[0])
        elif len(params) == 2:
            self._mapId = float(params[0])
            self._nbCharacters = int(params[1])

    @property
    def text(self) -> str:
        readableCriterionRef: str = I18n.getUiText("ui.criterion.MK", [self._mapId])
        return readableCriterionRef + " " + _operator.text + " " + self._nbCharacters

    def clone(self) -> IItemCriterion:
        return MapCharactersItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        nbCharacters: int = 0
        entitiesInfos: dict = None
        actorInfo: GameContextActorInformations = None
        entitiesFrame: RoleplayEntitiesFrame = (
            Kernel().getWorker().getFrame(RoleplayEntitiesFrame)
        )
        if entitiesFrame:
            entitiesInfos = entitiesFrame.entities
            for actorInfo in entitiesInfos:
                if isinstance(actorInfo, GameRolePlayCharacterInformations):
                    nbCharacters += 1
        return nbCharacters
