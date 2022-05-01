class Item:
    def __init__(self) -> None:
        self.__name: str = ""
        self.__runes: list[dict] = []

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value) -> None:
        self.__name = value

    @property
    def runes(self) -> list[dict]:
        return self.__runes

    @runes.setter
    def runes(self, value) -> None:
        self.__runes = value
