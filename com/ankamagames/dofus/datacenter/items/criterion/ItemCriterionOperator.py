class ItemCriterionOperator:

    SUPERIOR: str = ">"
    INFERIOR: str = "<"
    EQUAL: str = "="
    DIFFERENT: str = "!"
    OPERATORS_LIST: list = [
        SUPERIOR,
        INFERIOR,
        EQUAL,
        DIFFERENT,
        "#",
        "~",
        "s",
        "S",
        "e",
        "E",
        "v",
        "i",
        "X",
        "/",
    ]
    _operator: str

    def __init__(self, pstrOperator: str):
        super().__init__()
        self._operator = pstrOperator

    @property
    def text(self) -> str:
        return self._operator

    @property
    def htmlText(self) -> str:
        if self._operator == self.SUPERIOR:
            return "&gt"
        if self._operator == self.INFERIOR:
            return "&lt"
        return self._operator

    def compare(self, pLeftMember: float, pRightMember: float) -> bool:
        if self._operator == self.SUPERIOR:
            if pLeftMember > pRightMember:
                return True
        elif self._operator == self.INFERIOR:
            if pLeftMember < pRightMember:
                return True
        elif self._operator == self.EQUAL:
            if pLeftMember == pRightMember:
                return True
        elif self._operator == self.DIFFERENT:
            if pLeftMember != pRightMember:
                return True
        return False
