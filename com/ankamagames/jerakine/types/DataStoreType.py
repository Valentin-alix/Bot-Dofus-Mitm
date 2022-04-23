class JerakineError(Exception):
    pass


class DataStoreType:
    def __init__(
        self,
        sCategory: str,
        bPersistant: bool,
        nLocation: float = None,
        nBind: float = None,
    ):
        super().__init__()
        self._sCategory = sCategory
        self._bPersistant = bPersistant
        if bPersistant:
            if nLocation is None:
                raise JerakineError(
                    "When DataStoreType is a persistant data, arg 'nLocation' must be defined."
                )
            self._nLocation = nLocation
            if nBind is None:
                raise JerakineError(
                    "When DataStoreType is a persistant data, arg 'nBind' must be defined."
                )
            self._nBind = nBind
        self._ACCOUNT_ID: str = None
        self._CHARACTER_ID: str = None
        self._lastIdInitId = 0
        self._id = None

    @property
    def CHARACTER_ID(self) -> str:
        return DataStoreType._CHARACTER_ID

    @CHARACTER_ID.setter
    def CHARACTER_ID(self, value: str) -> None:
        self._CHARACTER_ID = value
        self._lastIdInitId += 1

    @property
    def ACCOUNT_ID(self) -> str:
        return self._ACCOUNT_ID

    @ACCOUNT_ID.setter
    def ACCOUNT_ID(self, value: str) -> None:
        self._ACCOUNT_ID = value
        self._lastIdInitId += 1

    @property
    def id(self) -> str:
        return self._id

    @property
    def category(self) -> str:
        return self._sCategory

    @property
    def persistant(self) -> bool:
        return self._bPersistant

    @property
    def location(self) -> int:
        return self._nLocation

    @property
    def bind(self) -> int:
        return self._nBind
