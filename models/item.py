class Item:
    def __init__(self):
        self.__name: str = ""
        self.__type_runes: list[str] = []
        self.__id_runes: list[int] = []
        self.__value_runes: list[int] = []
        self.__line_runes: list[int] = []
        self.__column_runes: list[int] = []
        self.__actual_values: list[int] = []
        self.__actual_id_values: list[int] = []

    def __len__(self):
        return len(self.__id_runes)

    @property
    def name(self):
        return self.__name

    @property
    def id_runes(self):
        return self.__id_runes

    @property
    def type_runes(self):
        return self.__type_runes

    @property
    def value_runes(self):
        return self.__value_runes

    @property
    def line_runes(self):
        return self.__line_runes

    @property
    def column_runes(self):
        return self.__column_runes

    @property
    def actual_values(self):
        return self.__actual_values

    @property
    def actual_id_values(self):
        return self.__actual_id_values

    @actual_id_values.setter
    def actual_id_values(self, value):
        self.__actual_id_values = value

    @actual_values.setter
    def actual_values(self, value):
        self.__actual_values = value

    @name.setter
    def name(self, value):
        self.__name = value

    @type_runes.setter
    def type_runes(self, value):
        self.__type_runes = value

    @value_runes.setter
    def value_runes(self, value):
        self.__value_runes = value

    @line_runes.setter
    def line_runes(self, value):
        self.__line_runes = value

    @column_runes.setter
    def column_runes(self, value):
        self.__column_runes = value

    @id_runes.setter
    def id_runes(self, value):
        self.__id_runes = value

    def clear_item(self):
        self.name = ""
        self.type_runes.clear()
        self.id_runes.clear()
        self.value_runes.clear()
        self.line_runes.clear()
        self.column_runes.clear()
