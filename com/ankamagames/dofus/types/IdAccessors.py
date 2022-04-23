from ast import FunctionType


class IdAccessors:

    _instanceById: FunctionType
    _allInstances: FunctionType

    def __init__(self, instanceById: FunctionType, allInstances: FunctionType):
        super().__init__()
        self._instanceById = instanceById
        self._allInstances = allInstances

    @property
    def instanceById(self) -> FunctionType:
        return self._instanceById

    @property
    def allInstances(self) -> FunctionType:
        return self._allInstances
