class Item:
    def __init__(self):
        self.__name = ""
        self.__type_rune = []
        self.__value_rune = []
        self.__line_rune = []
        self.__column_rune = []

    @property
    def name(self):
        return self.__name

    @property
    def type_rune(self):
        return self.__type_rune

    @property
    def value_rune(self):
        return self.__value_rune

    @property
    def line_rune(self):
        return self.__line_rune

    @property
    def column_rune(self):
        return self.__column_rune

    @name.setter
    def name(self, value):
        self.name = value

    @type_rune.setter
    def type_rune(self, value):
        self.type_rune = value

    @value_rune.setter
    def value_rune(self, value):
        self.value_rune = value

    @line_rune.setter
    def line_rune(self, value):
        self.line_rune = value

    @column_rune.setter
    def column_rune(self, value):
        self.column_rune = value
