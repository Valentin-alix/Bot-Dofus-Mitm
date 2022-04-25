class Item:
    def __init__(self):
        self.__name: str = ""
        self.__runes: list[dict] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def runes(self):
        return self.__runes

    @runes.setter
    def runes(self, value):
        self.__runes = value
