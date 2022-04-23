from models.data import Data


class Message:
    def __init__(self, message_id: int, data: Data):
        self.__message_id = message_id
        self.__data = data

    @property
    def message_id(self):
        return self.__message_id

    @property
    def data(self):
        return self.__data
