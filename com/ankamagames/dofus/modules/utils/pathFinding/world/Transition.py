class Transition:

    _type: int

    _direction: int

    _skillId: int

    _criterion: str

    _transitionMapId: float

    _cell: int

    _id: int

    def __init__(
        self,
        type: int,
        direction: int,
        skillId: int,
        criterion: str,
        transitionMapId: float,
        cell: int,
        id: int,
    ):
        super().__init__()
        self._type = type
        self._direction = direction
        self._skillId = skillId
        self._criterion = criterion
        self._transitionMapId = transitionMapId
        self._cell = cell
        self._id = id

    @property
    def type(self) -> int:
        return self._type

    @property
    def direction(self) -> int:
        return self._direction

    @property
    def skillId(self) -> int:
        return self._skillId

    @property
    def criterion(self) -> str:
        return self._criterion

    @property
    def cell(self) -> int:
        return self._cell

    @property
    def transitionMapId(self) -> float:
        return self._transitionMapId

    @property
    def id(self) -> int:
        return self._id

    def __str__(self) -> str:
        pass
