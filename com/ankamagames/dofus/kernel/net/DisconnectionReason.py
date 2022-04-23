class DisconnectionReason:

    _expected: bool

    _reason: int

    def __init__(self, expected: bool, reason: int):
        super().__init__()
        self._expected = expected
        self._reason = reason

    @property
    def expected(self) -> bool:
        return self._expected

    @property
    def reason(self) -> int:
        return self._reason
